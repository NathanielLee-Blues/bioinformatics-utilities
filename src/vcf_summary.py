#!/usr/bin/env python3

"""
Summarise a VCF file.
"""

import argparse
import csv
from pathlib import Path
from collections import Counter


def classify_variant(ref, alt):
    alt_alleles = alt.split(",")

    if len(ref) == 1 and all(len(a) == 1 for a in alt_alleles):
        return "SNP"

    return "indel_or_complex"


def parse_vcf(path):
    with open(path) as handle:
        for line in handle:
            if line.startswith("#"):
                continue

            fields = line.strip().split("\t")

            if len(fields) < 8:
                continue

            chrom, pos, variant_id, ref, alt, qual, filt, info = fields[:8]

            yield {
                "chromosome": chrom,
                "position": pos,
                "reference": ref,
                "alternate": alt,
                "quality": qual,
                "filter": filt,
                "variant_type": classify_variant(ref, alt),
            }


def summarise_variants(variants):
    variants = list(variants)

    type_counts = Counter(v["variant_type"] for v in variants)
    chrom_counts = Counter(v["chromosome"] for v in variants)
    pass_count = sum(1 for v in variants if v["filter"] == "PASS")

    summary_rows = [
        ("total_variants", len(variants)),
        ("PASS_variants", pass_count),
        ("SNP", type_counts.get("SNP", 0)),
        ("indel_or_complex", type_counts.get("indel_or_complex", 0)),
    ]

    for chrom, count in sorted(chrom_counts.items()):
        summary_rows.append((f"variants_on_{chrom}", count))

    return summary_rows


def write_csv(rows, output_path):
    with open(output_path, "w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["metric", "value"])
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description="Summarise variants in a VCF file.")
    parser.add_argument("vcf", help="Input VCF file")
    parser.add_argument("-o", "--output", help="Optional CSV output path")
    args = parser.parse_args()

    summary_rows = summarise_variants(parse_vcf(args.vcf))

    if args.output:
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        write_csv(summary_rows, args.output)

    for metric, value in summary_rows:
        print(f"{metric}: {value}")


if __name__ == "__main__":
    main()
