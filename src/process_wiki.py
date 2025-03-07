import pathlib
import json
from typing import IO, Callable
import networkx as nx
import hashlib
from collections import Counter
from itertools import chain
from tqdm import tqdm
import random

from datatrove.io import DataFolderLike
from datatrove.pipeline.readers import IpcReader, JsonlReader
from datatrove.executor import LocalPipelineExecutor
from datatrove.data import DocumentsPipeline
from datatrove.data import Document
from datatrove.pipeline.writers.disk_base import DiskWriter
from datatrove.pipeline.base import PipelineStep
from datatrove.data import DocumentsPipeline
from datatrove.pipeline.tokens.counter import TokensCounter
from datatrove.pipeline.readers.base import BaseDiskReader
from datatrove.utils.logging import logger

from utils import read_json, write_json, find_files
from morphology import decompose_tr, create_morph_graph, read_morph_graph, write_morph_graph, merge_morph_graphs, update_morph_graph, get_words, infer_best_decompositions_tr, read_tr_dictionary

TR_DICTIONARY = read_tr_dictionary()

MNT_DIR = "/mnt/u14157_ic_nlp_001_files_nfs"

if not pathlib.Path(MNT_DIR).exists():
    MNT_DIR = "/mnt"

DATA_DIR = f"{MNT_DIR}/nlpdata1/share/datasets/wikimedia___wikipedia/20231101.tr/0.0.0/b04c8d1ceb2f5cd4588862100d08de323dccfbaa"
DUMP_DATA_DIR = f"{MNT_DIR}/nlpdata1/home/ismayilz/project-morphgen/morph-gen-wiki"

# morphological analyzer apparently goes into infinite loop for these words :D
PROBLEMATIC_WORDS = ["çekoslovakyalılaştıramadıklarımızdan", "muvaffakiyetsizleştiricileştirilmeyi", "muvaffakiyetsizleştiricileştiriverebileceğini"]

def preprocessing_adapter(document: Document, source_file: str, id_in_file: str = None) -> DocumentsPipeline:
    return {
        "id": id_in_file,
        "text": document["text"].lower(),
        "metadata": {
            "url": document["url"],
            "file_stem": pathlib.Path(source_file).stem
        }
    }

class MorphSegmentation(PipelineStep):
    name = "🐿 Morph Segmenter"

    def __init__(self, output_folder: str = "./outputs"):
        super().__init__()
        self.output_folder = output_folder

    def run(self, data: DocumentsPipeline, rank: int = 0, world_size: int = 1) -> DocumentsPipeline:
        for document in data:
            with self.track_time():
                output_dir = pathlib.Path(f"{self.output_folder}/{document.metadata['file_stem']}")
                output_dir.mkdir(parents=True, exist_ok=True)
                document_id = hashlib.sha256(str(document.id).encode()).hexdigest()
                graph_path = output_dir / f"{document_id}.gml"

                if not graph_path.exists():
                    G = create_morph_graph()
                    words = get_words(document.text.lower())
                    for word in words:
                        if word in PROBLEMATIC_WORDS:
                            continue
                        # print(f"decomposing {word}")
                        decompositions = [d.to_json() for d in decompose_tr(word)]
                        decompositions = infer_best_decompositions_tr(word, decompositions, TR_DICTIONARY)
                        for decomposition in decompositions:
                            update_morph_graph(G, root=decomposition["root"], meta_morphemes=decomposition["meta_morphemes"], morphemes=decomposition["morphemes"])
                    self.stat_update("num_words", value=len(words))
                    nx.write_gml(G, str(graph_path))
                document.metadata["graph_path"] = str(graph_path)
            yield document

class MorphGraphMerger(DiskWriter):
    """Write data to datafolder (local or remote) in GML format

    Args:
        output_folder: a str, tuple or DataFolder where data should be saved
        output_filename: the filename to use when saving data, including extension. Can contain placeholders such as `${rank}` or metadata tags `${tag}`
        adapter: a custom function to "adapt" the Document format to the desired output format
    """
    name = "🐿 GML"

    def __init__(
        self,
        output_folder: DataFolderLike,
        output_filename: str = None,
        compression: str = None,
        adapter: Callable = None,
    ):
        super().__init__(output_folder, output_filename=output_filename, compression=compression, adapter=adapter, mode="wb")
        self.output_folder = output_folder
        self._graph_init = False

    def _write(self, document: dict, file_handler: IO, _filename: str):
        pathlib.Path(self.output_folder).mkdir(parents=True, exist_ok=True)
        merged_path = f"{self.output_folder}/{_filename}"
        G = read_morph_graph(document["metadata"]["graph_path"])
        GH = G

        if self._graph_init:
            H = read_morph_graph(merged_path)
            GH = merge_morph_graphs(G, H)

        write_morph_graph(GH, merged_path)
        self._graph_init = True

preprocessing = LocalPipelineExecutor(
    pipeline=[
        IpcReader(DATA_DIR, stream=True, progress=True, glob_pattern="*.arrow"),
        TokensCounter()
    ],
    logging_dir=f"{DUMP_DATA_DIR}/preprocessing_logs/",
    tasks=2,
    workers=2
)

morph_segmentation = LocalPipelineExecutor(
    pipeline=[
        JsonlReader(f"{DUMP_DATA_DIR}/batch_jsonl", progress=True, glob_pattern="*.jsonl", adapter=preprocessing_adapter),
        MorphSegmentation(output_folder=f"{DUMP_DATA_DIR}/morph_graphs")
    ],
    logging_dir=f"{DUMP_DATA_DIR}/morph_segment_logs/",
    tasks=540,
    workers=64
)

morph_merging = LocalPipelineExecutor(
    pipeline=[
        JsonlReader(f"{DUMP_DATA_DIR}/morph_graphs", progress=True, glob_pattern="*.jsonl.gz"),
        MorphSegmentation(output_folder=f"{DUMP_DATA_DIR}/morph_graphs"),
        # MorphGraphWriter(f"{DUMP_DATA_DIR}/morph_graphs_merged", "${file_stem}_${rank}.gml")
    ],
    logging_dir=f"{DUMP_DATA_DIR}/morph_merge_logs/",
    tasks=550,
    workers=64
)

def create_btwd_graph(btwd_data):
    btwd_graph = create_morph_graph()

    for sample in tqdm(btwd_data["data"], desc="Creating BTWD graph"):
        for decomposition in sample["decompositions"]:
            update_morph_graph(btwd_graph, decomposition["root"], decomposition["meta_morphemes"], decomposition["morphemes"], update_stats=False)

    return btwd_graph

def create_btwd_frequency(btwd_data):
    btwd_freq = {
        "roots": Counter(),
        "meta_morphemes": Counter(),
        "morphemes": Counter(),
        "meta_morpheme_compositions": Counter(),
        "morpheme_compositions": Counter()
    }

    for sample in tqdm(btwd_data["data"], desc="Creating BTWD freq data"):
        for decomposition in sample["decompositions"]:
            btwd_freq["roots"].update([decomposition["root"]])
            btwd_freq["meta_morphemes"].update(decomposition["meta_morphemes"])
            btwd_freq["morphemes"].update(decomposition["morphemes"])
    
    return btwd_freq

def process_single_wiki_for_btwd(btwd_data, train_file, initial_btwd_graph=None, initial_btwd_frequency=None):
    print(f"Starting BTWD processing for {train_file}")
    btwd_graph = initial_btwd_graph if initial_btwd_frequency else create_btwd_graph(btwd_data)
    btwd_frequency = initial_btwd_frequency if initial_btwd_frequency else create_btwd_frequency(btwd_data)
    
    print("Processing intersection of BTWD and train graphs")
    train_graph = read_morph_graph(train_file)
    intersection = nx.intersection(btwd_graph, train_graph)

    for node in intersection.nodes:
        if node.startswith("+"):
            btwd_frequency["meta_morphemes"].update([node[1:]])
            in_edges = train_graph.in_edges(node, keys=True)
            for in_edge in in_edges:
                edge_key = in_edge[2]
                last_morpheme = edge_key.split("+")[-1]
                btwd_frequency["morphemes"].update([last_morpheme])
        else:
            btwd_frequency["roots"].update([node])

    for edge in intersection.edges:
        btwd_edge_data = btwd_graph.get_edge_data(*edge)
        train_edge_data = train_graph.get_edge_data(*edge)
        nx.set_edge_attributes(btwd_graph, {edge: {"count": btwd_edge_data["count"]+train_edge_data["count"], "leaf": btwd_edge_data["leaf"]+train_edge_data["leaf"]}})

    def _update_freq_for_decomposition(freq_data, meta_morphemes, morphemes, ref_graph):
        meta_morpheme_composition = ""
        morpheme_composition = ""
        last_meta_morpheme_node = None

        for j, (meta_morpheme, morpheme) in enumerate(zip(meta_morphemes, morphemes)):
            meta_morpheme_node = f"+{meta_morpheme}"
            morpheme_node = f"+{morpheme}"

            if j == 0:
                last_meta_morpheme_node = meta_morpheme_node
                meta_morpheme_composition += meta_morpheme_node
                morpheme_composition += morpheme_node
                continue
            
            if last_meta_morpheme_node in ref_graph.nodes:
                neighbors = list(ref_graph.neighbors(last_meta_morpheme_node))

                if meta_morpheme_node in neighbors:
                    meta_morpheme_composition += meta_morpheme_node
                    morpheme_composition += morpheme_node
                    freq_data["meta_morpheme_compositions"].update([meta_morpheme_composition])
                    edges = ref_graph.adj[last_meta_morpheme_node][meta_morpheme_node]
                    
                    morpheme_composition_found = False
                    
                    for edge_key, _ in edges.items():
                        if morpheme_composition in edge_key:
                            freq_data["morpheme_compositions"].update([morpheme_composition])
                            morpheme_composition_found = True
                            break
                            
                    if not morpheme_composition_found:
                        break
                else:
                    break
            else:
                break
        
            last_meta_morpheme_node = meta_morpheme_node

    for sample in tqdm(btwd_data["data"], total=len(btwd_data["data"]), desc="Processing BTWD samples"):
        for decomposition in sample["decompositions"]:
            meta_morphemes = decomposition["meta_morphemes"]
            morphemes = decomposition["morphemes"]

            for k in range(len(meta_morphemes)):
                _update_freq_for_decomposition(btwd_frequency, meta_morphemes[k:], morphemes[k:], train_graph)

    return btwd_graph, btwd_frequency

def list_train_files():
    print("Gathering training morph graphs")
    train_files_path = pathlib.Path("train_files.txt")

    if train_files_path.exists():
        print("Using cached train files")
        with open("train_files.txt") as f:
            train_files = [line.strip() for line in f.readlines()]
    else:
        train_files = find_files(f"{DUMP_DATA_DIR}/morph_graphs", extension="gml")
        train_files = [file for file in train_files if not any([str(i).zfill(5) in file for i in range(530, 535)])]

        with open("train_files.txt", "w") as f:
            f.writelines([file+"\n" for file in train_files])
    
    return train_files

def process_wiki_for_btwd(btwd_path):
    btwd_path = pathlib.Path(btwd_path)
    btwd_data = read_json(btwd_path)
    status_file = "status.txt"

    btwd_graph = create_btwd_graph(btwd_data)
    btwd_frequency = create_btwd_frequency(btwd_data)

    write_morph_graph(btwd_graph, btwd_path.with_suffix(".gml"))
    train_files = list_train_files()

    for i, train_file in tqdm(enumerate(train_files), total=len(train_files), desc="Processing train files"):
        btwd_graph, btwd_frequency = process_single_wiki_for_btwd(btwd_data, train_file, initial_btwd_graph=btwd_graph, initial_btwd_frequency=btwd_frequency)

        if i % 100 == 0:
            write_json(btwd_frequency, btwd_path.parent / f"{btwd_path.stem}_freq.json")
            write_morph_graph(btwd_graph, btwd_path.with_suffix(".gml"))
            with open(status_file, "w") as f:
                f.write(f"{i+1}/{len(train_files)}")

    write_json(btwd_frequency, btwd_path.parent / f"{btwd_path.stem}_freq.json")
    write_morph_graph(btwd_graph, btwd_path.with_suffix(".gml"))
    with open(status_file, "w") as f:
        f.write(f"{len(train_files)}/{len(train_files)}")

def generate_btwd_documents(filepath: str):
    data = read_json(filepath)
    documents = []
    for i, (root, root_data) in enumerate(data["data"].items()):
        document = Document(text=root, id=i, metadata={"root_data": root_data})
        documents.append(document)
    return documents

def filter_decompositions(data: DocumentsPipeline, rank: int = 0, world_size: int = 1) -> DocumentsPipeline:
    pathlib.Path(f"{DUMP_DATA_DIR}/btwd_prep_filtered").mkdir(parents=True, exist_ok=True)
    
    for document in data:
        samples = []
        for derivation, derivation_data in tqdm(document.metadaqta["root_data"].items(), total=len(document.metadata["root_data"]), desc=f"Processing data for root {document.text}"):
            decompositions = infer_best_decompositions_tr(derivation, derivation_data, TR_DICTIONARY)
            if decompositions:
                samples.append({"root": document.text, "derivation": derivation, "decompositions": decompositions})
        write_json({"data": samples}, f"{DUMP_DATA_DIR}/btwd_prep_filtered/{document.id}.json")
        yield document

def generate_train_file_documents():
    train_files = list_train_files()
    documents = []
    for i, train_file in enumerate(train_files):
        document = Document(text=train_file, id=i)
        documents.append(document)
    return documents

class FileReader(BaseDiskReader):
    """Read file and return as document.

    Args:
        data_folder: the data folder to read from
        compression: the compression to use (default: "infer")
        limit: limit the number of JSON lines to read
        skip: skip the first n rows
        file_progress: show progress bar for files
        doc_progress: show progress bar for documents
        adapter: function to adapt the data dict from the source to a Document.
            Take as input: data: dict, path: str, id_in_file: int | str
            Return: a dict with at least a "text" key
        text_key: key to use for the text in the default adapter (default: "text"). Ignored if you provide your own `adapter`
        id_key: key to use for the id in the default adapter (default: "id"). Ignored if you provide your own `adapter`
        default_metadata: default metadata to add to all documents
        recursive: if True, will read files recursively in subfolders (default: True)
        glob_pattern: a glob pattern to filter files to read (default: None)
        shuffle_files: shuffle the files within the returned shard. Mostly used for data viz. purposes, do not use
            with dedup blocks
    """

    name = "🐿 File Reader"

    def __init__(
        self,
        data_folder: DataFolderLike,
        compression: str = "infer",
        limit: int = -1,
        skip: int = 0,
        progress: bool = False,
        adapter: Callable = None,
        text_key: str = "text",
        id_key: str = "id",
        default_metadata: dict = None,
        recursive: bool = True,
        glob_pattern: str = None,
        shuffle_files: bool = False,
    ):
        super().__init__(
            data_folder,
            limit,
            skip,
            progress,
            adapter,
            text_key,
            id_key,
            default_metadata,
            recursive,
            glob_pattern,
            shuffle_files,
        )
        self.compression = compression
        self.train_files = list_train_files()

    def run(self, data: DocumentsPipeline = None, rank: int = 0, world_size: int = 1) -> DocumentsPipeline:
        """
        Will get this rank's shard and sequentially read each file in the shard, yielding Document.
        Args:
            data: any existing data from previous pipeline stages
            rank: rank of the current task
            world_size: total number of tasks

        Returns:

        """
        if data:
            yield from data
        files_shard = self.train_files[rank::world_size]
        if len(files_shard) == 0:
            if rank == 0:
                raise RuntimeError(f"No files found on {self.data_folder.path}!")
            # otherwise just a warning
            logger.warning(f"No files found on {self.data_folder.path} for {rank=}")
        if self.shuffle_files:
            random.shuffle(files_shard)
        for doc in self.read_files_shard(files_shard):
            self.update_doc_stats(doc)
            yield doc

    def read_file(self, filepath: str):
        file = pathlib.Path(filepath)
        yield Document(text=filepath, id=file.stem)

class BTWDProcessor(PipelineStep):
    name = "🐿 BTWD Processor"

    def __init__(self, btwd_path, output_folder: str = "./outputs"):
        super().__init__()
        self.btwd_data = read_json(btwd_path)
        self.output_dir = pathlib.Path(output_folder)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.freq_dir = self.output_dir / "freqs"
        self.graph_dir = self.output_dir / "graphs"
        self.freq_dir.mkdir(parents=True, exist_ok=True)
        self.graph_dir.mkdir(parents=True, exist_ok=True)

    def run(self, data: DocumentsPipeline, rank: int = 0, world_size: int = 1) -> DocumentsPipeline:
        for document in data:
            with self.track_time():
                if document.text:
                    train_subdir = document.text.split("/")[-2]
                    pathlib.Path(self.freq_dir / train_subdir).mkdir(parents=True, exist_ok=True)
                    pathlib.Path(self.graph_dir / train_subdir).mkdir(parents=True, exist_ok=True)
                    btwd_graph, btwd_frequency = process_single_wiki_for_btwd(self.btwd_data, document.text)
                    write_json(btwd_frequency, self.freq_dir / train_subdir / f"{document.id}_freq.json")
                    write_morph_graph(btwd_graph, self.graph_dir / train_subdir / f"{document.id}_graph.gml")

btwd_filtering = LocalPipelineExecutor(
    pipeline=[
        generate_btwd_documents(f"{MNT_DIR}/nlpdata1/home/ismayilz/project-morphgen/morph-gen/data/tr/bilkent-turkish-writings/btwd_prep.json"),
        filter_decompositions
    ],
    logging_dir=f"{DUMP_DATA_DIR}/btwd_filtering_logs/",
    tasks=15060,
    workers=64
)

btwd_wiki_processing = LocalPipelineExecutor(
    pipeline=[
        FileReader(f"{DUMP_DATA_DIR}/morph_graphs", glob_pattern="**/*.gml", progress=True),
        BTWDProcessor("../data/tr/bilkent-turkish-writings/btwd_prep_post_raw.json", f"{DUMP_DATA_DIR}/btwd_prep_post_wiki_processed")
    ],
    logging_dir=f"{DUMP_DATA_DIR}/btwd_processing_logs/",
    tasks=530000,
    workers=64
)
if __name__ == "__main__":
    # preprocessing.run()
    # morph_segmentation.run()
    # process_wiki_for_btwd("../data/tr/bilkent-turkish-writings/btwd_default_final_raw.json")
    # btwd_filtering.run()
    btwd_wiki_processing.run()