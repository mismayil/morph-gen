import pathlib
import json
from typing import IO, Callable
from io import UnsupportedOperation
import networkx as nx
import hashlib

from datatrove.io import DataFolderLike, get_datafolder
from datatrove.pipeline.readers import IpcReader, JsonlReader
from datatrove.executor import LocalPipelineExecutor
from datatrove.data import DocumentsPipeline
from langdetect import detect_langs
from datatrove.data import Document
from datatrove.pipeline.filters.base_filter import BaseFilter
from datatrove.pipeline.writers.disk_base import DiskWriter
from datatrove.pipeline.writers.jsonl import JsonlWriter
from datatrove.pipeline.base import PipelineStep
from datatrove.data import DocumentsPipeline

from utils import generate_unique_id
from morphology import (
    decompose_tr,
    create_morph_graph,
    read_morph_graph,
    write_morph_graph,
    merge_morph_graphs,
    update_morph_graph,
    get_words,
)

DATA_DIR = "/mnt/nlpdata1/share/datasets/allenai___c4/tr/0.0.0/1588ec454efa1a09f29cd18ddd04fe05fc8653a2"
DUMP_DATA_DIR = "/mnt/nlpdata1/home/ismayilz/morph-gen-c4"


def preprocessing_adapter(
    document: Document, source_file: str, id_in_file: str = None
) -> DocumentsPipeline:
    return {
        "id": id_in_file,
        "text": document["text"].lower(),
        "metadata": {
            "url": document["url"],
            "timestamp": str(document["timestamp"]),
            "file_stem": pathlib.Path(source_file).stem,
        },
    }


class TRLanguageFilter(BaseFilter):
    name = "🌍 Language ID"
    _requires_dependencies = ["langdetect"]

    def __init__(
        self,
        language_threshold: float = 0.9,
        exclusion_writer: DiskWriter = None,
    ):
        super().__init__(exclusion_writer)
        self.language_threshold = language_threshold
        self._model = None

    def filter(self, doc: Document) -> bool:
        tr_score = 0

        try:
            lang_scores = detect_langs(doc.text)

            for lang_score in lang_scores:
                if lang_score.lang == "tr":
                    tr_score = float(lang_score.prob)
        except Exception as e:
            pass

        doc.metadata["tr_score"] = tr_score
        return tr_score > self.language_threshold


class MorphSegmentation(PipelineStep):
    name = "🐿 Morph Segmenter"

    def __init__(self, output_folder: str = "./outputs"):
        super().__init__()
        self.output_folder = output_folder

    def run(
        self, data: DocumentsPipeline, rank: int = 0, world_size: int = 1
    ) -> DocumentsPipeline:
        for document in data:
            with self.track_time():
                output_dir = pathlib.Path(
                    f"{self.output_folder}/{document.metadata['file_stem']}"
                )
                output_dir.mkdir(parents=True, exist_ok=True)
                document_id = hashlib.sha256(str(document.id).encode()).hexdigest()
                graph_path = output_dir / f"{document_id}.gml"

                if not graph_path.exists():
                    G = create_morph_graph()
                    words = get_words(document.text)
                    for word in words:
                        decompositions = decompose_tr(word)
                        for decomposition in decompositions:
                            update_morph_graph(
                                G,
                                root=decomposition.root,
                                meta_morphemes=decomposition.meta_morphemes,
                                morphemes=decomposition.morphemes,
                            )
                    self.stat_update("num_words", value=len(words))
                    nx.write_gml(G, str(graph_path))
                document.metadata["graph_path"] = str(graph_path)
            yield document


class MorphGraphWriter(DiskWriter):
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
        super().__init__(
            output_folder,
            output_filename=output_filename,
            compression=compression,
            adapter=adapter,
            mode="wb",
        )
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
        IpcReader(
            DATA_DIR,
            stream=True,
            progress=True,
            glob_pattern="*.arrow",
            adapter=preprocessing_adapter,
        ),
        TRLanguageFilter(
            exclusion_writer=JsonlWriter(
                f"{DUMP_DATA_DIR}/lang_filter_removed", "${file_stem}_${rank}.jsonl"
            )
        ),
        JsonlWriter(f"{DUMP_DATA_DIR}/lang_filtered", "${file_stem}_${rank}.jsonl"),
    ],
    logging_dir=f"{DUMP_DATA_DIR}/preprocessing_logs/",
    tasks=600,
    workers=64,
)

morph_segmentation = LocalPipelineExecutor(
    pipeline=[
        JsonlReader(
            f"{DUMP_DATA_DIR}/lang_filtered", progress=True, glob_pattern="*.jsonl.gz"
        ),
        MorphSegmentation(output_folder=f"{DUMP_DATA_DIR}/morph_graphs"),
    ],
    logging_dir=f"{DUMP_DATA_DIR}/morph_segment_logs/",
    tasks=550,
    workers=64,
)

# morph_merging = LocalPipelineExecutor(
#     pipeline=[
#         JsonlReader(f"{DUMP_DATA_DIR}/lang_filtered", progress=True, glob_pattern="*.jsonl.gz"),
#         MorphSegmentation(output_folder=f"{DUMP_DATA_DIR}/morph_graphs"),
#         MorphGraphWriter(f"{DUMP_DATA_DIR}/morph_graphs_merged", "${file_stem}_${rank}.gml")
#     ],
#     logging_dir=f"{DUMP_DATA_DIR}/morph_merge_logs/",
#     tasks=550,
#     workers=64
# )

if __name__ == "__main__":
    # preprocessing.run()
    morph_segmentation.run()
    # morph_merging.run()
