import json
import sys


def main():
    filename = sys.argv[1]
    with open(filename, "r") as f:
        fin_data = json.load(f)

    metadata = fin_data["metadata"]
    json_lines = fin_data["data"]

    # for each dict in json_lines, split segmentation fields on hyphens
    out_lines = []

    for line in json_lines:
        line_copy = line.copy()

        for segm_col in ["segments", "prefixes", "suffixes"]:
            if len(line[segm_col]) > 0:
                line_copy[segm_col] = line[segm_col].split("-")
            else:
                line_copy[segm_col] = []

        out_lines.append(line_copy)

    output = {}
    output["metadata"] = metadata
    output["data"] = out_lines

    print(json.dumps(output, ensure_ascii=False))


if __name__ == "__main__":
    main()
