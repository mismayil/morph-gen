#!/usr/bin/env python

import json

import click
import pandas as pd


@click.command()
@click.argument("input_file", type=click.Path(exists=True))
def main(input_file):

    data = pd.read_csv(input_file, sep="\t")
    words = data.word.tolist()
    segments = data.segments.str.split("-").tolist()
    sentences = data.sentence.tolist()
    lemmas = data.lemma.tolist()
    pos_tags = data.pos.tolist()
    suffixes = data.suffix.tolist()

    json_lines = []

    for word, segment_list, sentence, lemma, pos_tag, suffix in zip(
        words, segments, sentences, lemmas, pos_tags, suffixes
    ):
        json_line_dict = {
            "derivation": word,
            "morphemes": segment_list,
            "meta_morphemes": [],
            "sentence": sentence,
            "root": lemma,
            "pos": pos_tag,
        }
        json_lines.append(json_line_dict)

    output = {
        "metadata": {
            "source": input_file,
            "processor": "none",
            "language": "fi",
            "size": len(json_lines),
        },
        "data": json_lines,
    }

    with click.get_text_stream("stdout") as output_stream:
        output_stream.write(json.dumps(output, ensure_ascii=False))


if __name__ == "__main__":
    main()
