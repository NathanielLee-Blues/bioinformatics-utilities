#!/usr/bin/env python3

"""
Calculate basic read and quality statistics for a FASTQ file.
"""

import argparse
import csv
from pathlib import Path


def phred33_to_score(char):
    return ord(char) - 33


def parse_fastq(path):
    with open(path) as handle:
        while True:
            header = handle.readline().strip()
            sequence = handle.readline().strip()
            plus = handle.readline().strip()
            quality = handle.readline().strip()

            if not header:
                break

            if not header.startswith("@") or plus != "+":
                raise ValueError("Invalid FASTQ format detected.")

            if len(sequence) != len(quality):
                raise ValueError("FASTQ sequence and quality lengths do not match.")

            yield header[1:], sequence, quality


def calculate_qc(records):
    reads = list(records)

    if not reads:
        raise ValueError("No FASTQ reads found.")

    lengths = [len(seq) for _, seq, _ in reads]
    all_quality_scores = [
        phred33_to_score(char)
        for _, _, quality in reads
        for char in quality
    ]

    return {
        "read_count": len(reads),
        "total_bases": sum(lengths),
        "min_read_length": min(lengths),
        "max_read_length": max(lengths),
        "mean_read_length": round(sum(lengths) / len(lengths), 2),
        "mean_phred_quality": round(sum(all_quality_scores) / len(all_quality_scores), 2),
    }


def write_csv(stats, output_path):
    with open(output_path, "w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["metric", "value"])
        for key, value in stats.items():
            writer.writerow([key, value])


def main():
    parser = argparse.ArgumentParser(description="Calculate basic FASTQ QC statistics.")
    parser.add_argument("fastq", help="Input FASTQ file")
    parser.add_argument("-o", "--output", help="Optional CSV output path")
    args = parser.parse_args()

    stats = calculate_qc(parse_fastq(args.fastq))

    if args.output:
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        write_csv(stats, args.output)

    for key, value in stats.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
