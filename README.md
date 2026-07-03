# Bioinformatics Utilities

![Python](https://img.shields.io/badge/Python-Command--line%20utilities-blue)
![Bioinformatics](https://img.shields.io/badge/Bioinformatics-FASTA%20FASTQ%20VCF-purple)

## Project overview

This repository contains a small collection of Python command-line utilities for working with common bioinformatics file formats.

The project uses real input files from a bacterial variant-calling workflow, including:

- an E. coli reference genome in FASTA format
- subsetted paired-end E. coli FASTQ reads
- a filtered VCF containing candidate variants

The aim is to demonstrate practical Python scripting, file parsing, command-line tool design, and basic testing using real bioinformatics data.

## Tools included

| Tool | Purpose | Input | Output |
|---|---|---|---|
| `fasta_stats.py` | Calculates summary statistics for a FASTA file | FASTA | Printed summary and optional CSV |
| `fastq_basic_qc.py` | Calculates basic read and quality statistics for a FASTQ file | FASTQ | Printed summary and optional CSV |
| `vcf_summary.py` | Summarises variants in a VCF file | VCF | Printed summary and optional CSV |
| `reverse_complement.py` | Generates the reverse complement of a DNA sequence | DNA sequence | Reverse-complement sequence |

## Tool descriptions and uses

### `fasta_stats.py`

This utility reads a FASTA file and calculates basic sequence-level statistics.

It reports:

- number of sequences
- total sequence length
- minimum sequence length
- maximum sequence length
- mean sequence length
- GC percentage

This is useful when checking a reference genome, contig file, transcriptome assembly, or any FASTA file where sequence length and GC content matter.

Example use:

~~~bash
python3 src/fasta_stats.py data/inputs/reference/ecoli_rel606_reference.fasta -o results/fasta_stats.csv
~~~

In this project, the FASTA utility summarised the E. coli REL606 reference genome:

| Metric | Value |
|---|---:|
| Sequence count | 1 |
| Total length | 4,629,812 |
| GC percentage | 50.77% |

---

### `fastq_basic_qc.py`

This utility reads a FASTQ file and calculates basic read-level quality statistics.

It reports:

- read count
- total bases
- minimum read length
- maximum read length
- mean read length
- mean Phred quality score

This is useful for quick inspection of sequencing reads before running a full quality-control tool such as FastQC or MultiQC. It is not intended to replace those tools, but it demonstrates how FASTQ parsing and Phred quality scoring work.

Example use:

~~~bash
python3 src/fastq_basic_qc.py data/inputs/reads/SRR2584866_R1_1000_reads.fastq -o results/fastq_qc_R1.csv
python3 src/fastq_basic_qc.py data/inputs/reads/SRR2584866_R2_1000_reads.fastq -o results/fastq_qc_R2.csv
~~~

In this project, the FASTQ utility summarised 1,000 reads from each paired-end file:

| File | Reads | Total bases | Mean read length | Mean Phred quality |
|---|---:|---:|---:|---:|
| R1 | 1,000 | 127,430 | 127.43 | 35.22 |
| R2 | 1,000 | 131,415 | 131.41 | 35.55 |

---

### `vcf_summary.py`

This utility reads a VCF file and summarises candidate variants.

It reports:

- total number of variants
- number of PASS variants
- number of SNPs
- number of indel or complex variants
- variant counts per chromosome or contig

This is useful for quickly checking the output of a variant-calling workflow and confirming the balance of SNPs and indels in a filtered VCF.

Example use:

~~~bash
python3 src/vcf_summary.py data/inputs/variants/SRR2584866_filtered_variants.vcf -o results/vcf_summary.csv
~~~

In this project, the VCF utility summarised filtered candidate variants from the E. coli workflow:

| Metric | Value |
|---|---:|
| Total variants | 407 |
| PASS variants | 407 |
| SNPs | 353 |
| Indel or complex variants | 54 |
| Variants on CP000819.1 | 407 |

---

### `reverse_complement.py`

This utility returns the reverse complement of a DNA sequence.

It supports standard DNA bases:

- A
- T
- G
- C
- N

This is useful for simple sequence checks, primer/probe work, and demonstrating basic sequence manipulation in Python.

Example use:

~~~bash
python3 src/reverse_complement.py ATGCCGTA
~~~

Output:

~~~text
TACGGCAT
~~~

## Input data

The project uses real input files copied or subsetted from the `variant-calling-workflow` project.

| File | Description |
|---|---|
| `data/inputs/reference/ecoli_rel606_reference.fasta` | E. coli REL606 reference genome |
| `data/inputs/reads/SRR2584866_R1_1000_reads.fastq` | First 1,000 reads from a real R1 FASTQ file |
| `data/inputs/reads/SRR2584866_R2_1000_reads.fastq` | First 1,000 reads from a real R2 FASTQ file |
| `data/inputs/variants/SRR2584866_filtered_variants.vcf` | Filtered VCF from the variant-calling workflow |

The FASTQ files are subsetted so the repository remains lightweight while still using real sequencing reads.

## How to prepare the inputs

The input files are prepared using:

~~~bash
bash scripts/prepare_inputs.sh
~~~

This script copies the reference FASTA and filtered VCF from the variant-calling workflow project, and creates 1,000-read FASTQ subsets from the paired-end reads.

## How to run all utilities

~~~bash
python3 src/fasta_stats.py data/inputs/reference/ecoli_rel606_reference.fasta -o results/fasta_stats.csv

python3 src/fastq_basic_qc.py data/inputs/reads/SRR2584866_R1_1000_reads.fastq -o results/fastq_qc_R1.csv

python3 src/fastq_basic_qc.py data/inputs/reads/SRR2584866_R2_1000_reads.fastq -o results/fastq_qc_R2.csv

python3 src/vcf_summary.py data/inputs/variants/SRR2584866_filtered_variants.vcf -o results/vcf_summary.csv

python3 src/reverse_complement.py ATGCCGTA > results/reverse_complement_example.txt
~~~

## Testing

A simple standard-library test runner is included:

~~~bash
python3 tests/run_tests.py
~~~

The tests check that each utility runs successfully and returns expected values for the real input files.

## Repository structure

~~~text
bioinformatics-utilities/
├── data/
│   └── inputs/
│       ├── reference/
│       ├── reads/
│       └── variants/
├── src/
│   ├── fasta_stats.py
│   ├── fastq_basic_qc.py
│   ├── vcf_summary.py
│   └── reverse_complement.py
├── tests/
│   └── run_tests.py
├── scripts/
│   └── prepare_inputs.sh
├── results/
├── docs/
├── requirements.txt
└── README.md
~~~

## Skills demonstrated

This project demonstrates:

- Python command-line scripting
- FASTA parsing
- FASTQ parsing
- VCF parsing
- Phred quality score handling
- simple sequence manipulation
- CSV output generation
- standard-library testing
- reusable bioinformatics utility design
- clear project documentation

## Limitations

These utilities are intentionally lightweight and educational.

They are useful for small files, quick checks, and demonstrating file parsing logic, but they are not replacements for mature production tools such as FastQC, MultiQC, BCFtools, SAMtools, or Biopython-based pipelines.

For more detail, see [`docs/LIMITATIONS.md`](docs/LIMITATIONS.md).

