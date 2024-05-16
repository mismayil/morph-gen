import argparse

from transformers import AutoTokenizer
from datasets import load_dataset

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--model", type=str, default="gpt2")
    parser.add_argument("-o", "--output", type=str, default="tokenizer")
    parser.add_argument("-d", "--dataset", type=str, default="mismayil/tr_wikipedia")
    parser.add_argument("-c", "--cache_dir", type=str, default=".cache")

    args = parser.parse_args()
    
    dataset = load_dataset(args.dataset, cache_dir=args.cache_dir)
    tokenizer = AutoTokenizer.from_pretrained(args.model)
    tokenizer.train_from_iterator(dataset["train"]["text"])
    tokenizer.save_pretrained(args.output)

if __name__ == '__main__':
    main()