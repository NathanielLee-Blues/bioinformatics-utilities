# Methods

## Data preparation

Input files are prepared using:

    bash scripts/prepare_inputs.sh

This script copies real input files from the `variant-calling-workflow` project and creates lightweight FASTQ subsets for use in this repository.

The prepared inputs are stored under:

    data/inputs/

## FASTA statistics

The `fasta_stats.py` script parses a FASTA file and calculates:

- sequence count
- total sequence length
- minimum sequence length
- maximum sequence length
- mean sequence length
- GC percentage

GC percentage is calculated from the number of G and C bases divided by the total number of bases.

## FASTQ basic QC

The `fastq_basic_qc.py` script parses FASTQ records and calculates:

- read count
- total bases
- minimum read length
- maximum read length
- mean read length
- mean Phred quality score

The script assumes Phred+33 quality encoding.

## VCF summary

The `vcf_summary.py` script parses non-header VCF records and reports:

- total variants
- PASS variants
- SNP count
- indel or complex variant count
- variants per chromosome or contig

Variants are classified as SNPs when the reference allele and all alternate alleles are single bases. Otherwise, they are classified as indel or complex.

## Reverse complement

The `reverse_complement.py` script accepts a DNA sequence and returns the reverse complement.

It supports:

- A
- T
- G
- C
- N

Lowercase input is accepted and output is returned in uppercase.

## Testing

The test runner is:

    tests/run_tests.py

It uses only the Python standard library and checks that all utilities run successfully on the prepared input files.
