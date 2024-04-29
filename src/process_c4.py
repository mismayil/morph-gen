import argparse
import multiprocessing
from datasets import load_dataset
from tqdm import tqdm
import spacy
import pathlib
from spacy.symbols import dobj, nmod, amod, advmod, pobj, prep, NOUN, VERB
import re

from utils import write_jsonl, find_files

compound = 7037928807040764755

DATA_DIR = "/mnt/u14157_ic_nlp_001_files_nfs/nlpdata1/share/datasets/allenai___json/en-139638ded39e9288/0.0.0/8bb11242116d547c741b2e8a1f18598ffdd40a1d4f2a2872c7a28b697434bc96"

nlp = spacy.load("en_core_web_lg", exclude=["ner"])

def process_sentence(sentence):
    doc = nlp(sentence)
    ngrams = []

    for token in doc:
        if not token.is_stop:
            if token.dep == dobj and token.pos == NOUN:
                ngrams.append((token.head.lemma_.lower(), token.lemma_.lower()))
            elif token.dep in [nmod, amod, advmod, compound]:
                if token.head.pos in [NOUN, VERB]:
                    ngrams.append((token.lemma_.lower(), token.head.lemma_.lower()))
            elif token.dep == pobj and token.head and token.head.dep == prep and token.head.head:
                ngrams.append((token.head.head.lemma_.lower(), token.head.lemma_.lower(), token.lemma_.lower()))

    return ngrams

def process_sample(sample, source_file, sample_idx):
    sample_data = {}
    doc = nlp(sample["text"])
    file_pattern = r"json-(?P<split>train|validation)-(?P<fnum>\d+)-of-(?P<mnum>\d+).arrow"

    match = re.fullmatch(file_pattern, source_file)
    file_name = source_file

    if match:
        file_num = match.group("fnum")
        max_num = match.group("mnum")
        split = "val" if match.group("split") == "validation" else "train"
        file_name = f"{split}-{file_num}-{max_num}"
    
    for sent_idx, sent in enumerate(doc.sents):
        ngrams = [" ".join(ngram) for ngram in process_sentence(sent.text)]
        
        for ngram in ngrams:
            if ngram not in sample_data:
                sample_data[ngram] = {"count": 0, "sources": []}
            sample_data[ngram]["count"] += 1
            sample_data[ngram]["sources"].append(f"file={file_name},sample={sample_idx},sent={sent_idx}")
    
    return sample_data

def merge_results(results):
    merged_results = {}

    for result in results:
        for ngram, ngram_data in result.items():
            if ngram not in merged_results:
                merged_results[ngram] = {"count": 0, "sources": []}
            merged_results[ngram]["count"] += ngram_data["count"]
            merged_results[ngram]["sources"].extend(ngram_data["sources"])
    
    return merged_results

def process_c4_file(data_path, output_dir):
    data_path = pathlib.Path(data_path)
    data_dir = str(data_path.parent)
    data_file = str(data_path.name)
    data = load_dataset(data_dir, data_files=data_file, streaming=True)
    data = data["validation"] if "validation" in data else data["train"]
    results = []
    data_len = sum([1 for _ in iter(data)])

    output_dir = pathlib.Path(f"{output_dir}/results/results_{data_path.stem}")
    output_dir.mkdir(parents=True, exist_ok=True)
    process_status_file = open(output_dir / "process_status.txt", "w", encoding="utf-8")

    for sample_idx, sample in tqdm(enumerate(iter(data)), total=data_len, leave=True, position=0, desc=f"Processing C4 file: {data_file}", file=process_status_file):
        result = process_sample(sample, data_file, sample_idx)
        results.append(result)
    
    process_status_file.write("\nProcessing done.")
    process_status_file.close()

    merged_results = merge_results(results)

    batch_size = 10000
    num_batches = (len(merged_results) // batch_size) + 1

    merged_results = list(merged_results.items())

    merge_status_file = open(output_dir / "merge_status.txt", "w", encoding="utf-8")

    for i in tqdm(range(num_batches), total=num_batches, desc="Merging results", leave=True, position=0, file=merge_status_file):
        start = i * batch_size
        end = (i + 1) * batch_size
        results_batch = merged_results[start:end]
        if results_batch:
            write_jsonl([{"ngram": ngram, **ngram_data} for ngram, ngram_data in results_batch], output_dir / f"results_{data_path.stem}-batch{i}.jsonl")

    merge_status_file.write("\nMerging done.")
    merge_status_file.close()

def process_c4_batch(data_paths, output_dir, batch_num=0):
    status_dir = pathlib.Path(f"{output_dir}/status")
    status_dir.mkdir(parents=True, exist_ok=True)
    batch_status_file = open(status_dir / f"batch{batch_num}_status.txt", "w", encoding="utf-8")
    
    for data_path in tqdm(data_paths, total=len(data_paths), desc=f"Processing C4 batch {batch_num}", leave=True, position=0, file=batch_status_file):
        process_c4_file(data_path, output_dir)

def process_c4(data_paths, output_dir):
    num_cores = multiprocessing.cpu_count()
    num_cores = num_cores - int(num_cores * 0.10)
    batch_size = (len(data_paths) // num_cores) + 1

    procs = []

    for i in range(num_cores):
        start = i * batch_size
        end = (i + 1) * batch_size
        data_paths_batch = data_paths[start:end]
        
        if data_paths_batch:
            p = multiprocessing.Process(target=process_c4_batch, args=(data_paths_batch, output_dir, i))
            p.start()
            procs.append(p)
    
    for p in procs:
        p.join()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--data-dir", type=str, default=DATA_DIR)
    parser.add_argument("-o", "--output-dir", type=str, default="data")

    args = parser.parse_args()

    data_paths = find_files(args.data_dir, extension=".arrow")
    process_c4(data_paths, args.output_dir)

if __name__ == "__main__":
    main()