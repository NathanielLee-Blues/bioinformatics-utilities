# Project plan

## Project title

Bioinformatics Utilities

## Purpose

This project provides a small collection of Python command-line utilities for working with common bioinformatics file formats.

The aim is to demonstrate practical Python scripting, file parsing, command-line tool design, CSV output generation, and basic testing using real bioinformatics inputs.

## Input data

The project uses real files copied or subsetted from the variant-calling workflow project:

- E. coli REL606 reference genome in FASTA format
- subsetted real paired-end E. coli FASTQ reads
- filtered VCF from the variant-calling workflow

## Utilities

The first version includes four utilities:

1. `fasta_stats.py` — calculates FASTA sequence statistics.
2. `fastq_basic_qc.py` — calculates basic FASTQ read and quality statistics.
3. `vcf_summary.py` — summarises VCF variant calls.
4. `reverse_complement.py` — generates the reverse complement of a DNA sequence.

## Planned outputs

- FASTA statistics CSV
- FASTQ QC CSV for R1 reads
- FASTQ QC CSV for R2 reads
- VCF summary CSV
- reverse-complement example output
- standard-library test runner output

## Portfolio value

This project demonstrates Python scripting skills that are directly relevant to bioinformatics roles, including parsing FASTA, FASTQ, and VCF files; writing reusable command-line tools; generating structured outputs; and testicat > docs/PROJECT_PLAN.md <<'EOF'
# Project plan

## Project title

Bioinformatics Utilities

## Purpose

This project provides a small collection of Python command-line utilities for working with common bioinformatics file formats.

The aim is to demonstrate practical Python scripting, file parsing, command-line tool design, CSV output generation, and basic testing using real bioinformatics inputs.

## Input data

The project uses real files copied or subsetted from the variant-calling workflow project:

- E. coli REL606 reference genome in FASTA format
- subsetted real paired-end E. coli FASTQ reads
- filtered VCF from the variant-calling workflow

## Utilities

The first version includes four utilities:

1. `fasta_stats.py` — calculates FASTA sequence statistics.
2. `fastq_basic_qc.py` — calculates basic FASTQ read and quality statistics.
3. `vcf_summary.py` — summarises VCF variant calls.
4. `reverse_complement.py` — generates the reverse complement of a DNA sequence.

## Planned outputs

- FASTA statistics CSV
- FASTQ QC CSV for R1 reads
- FASTQ QC CSV for R2 reads
- VCF summary CSV
- reverse-complement example output
- standard-library test runner output

