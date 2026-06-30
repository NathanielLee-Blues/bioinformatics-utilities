#!/usr/bin/env python3

"""
Calculate basic statistics for a FASTA file.
"""

import argparse
import csv
from pathlib import Path


def parse_fasta(path):
    name = None
    sequence_parts = []

    with open(path) as handle:
        for line in handle:
            line = line.strip()

            if not line:
                continue

            if line.startswith(">"):
                if name is not None:
                    yield name, "".join(sequence_parts)

                name = line[1:].split()[0]
                sequence_parts = []
            else:
                sequence_parts.append(line.upper())

        if name is not None:
            yield name, "".join(sequence_parts)


def calculate_stats(records):
    sequences = [seq for _, seq in records]

    if not sequences:
        raise ValueError("No FASTA sequences found.")

    lengths = [len(seq) for seq in sequences]
    total_bases = sum(lengths)
    gc_bases = sum(seq.count("G") + seq.count("C") for seq in sequences)

    return {
        "sequence_count": len(sequences),
        "total_length": total_bases,
        "min_length": min(lengths),
        "max_length": max(lengths),
        "mean_length": round(total_bases / len(sequences), 2),
        "gc_percent": round((gc_bases / total_bases) * 100, 2) if total_bases else 0,
    }


def write_csv(stats, output_path):
    with open(output_path, "w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["metric", "value"])
        for key, value in stats.items():
            writer.writerow([key, value])


def main():
    parser = argparse.ArgumentParser(description="Calculate basic FASTA statistics.")
    parser.add_argument("fasta", help="Input FASTA file")
    parser.add_argument("-o", "--output", help="Optional CSV output path")
    args = parser.parse_args()

    records = list(parse_fasta(args.fasta))
    stats = calculate_stats(records)

    if args.output:
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        write_csv(stats, args.output)

    for key, value in stats.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
