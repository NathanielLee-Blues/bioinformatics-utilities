# Project plan and scope

## Objective

Create a small set of readable Python command-line tools that explain and verify basic operations on FASTA, FASTQ and VCF data using real inputs.

## Questions

1. Can common file formats be parsed without hiding the logic behind a large framework?
2. Which summary statistics are useful for a first-pass check of each format?
3. Can the tools provide both terminal output and machine-readable CSV results?
4. Which limitations make dedicated production software preferable for larger analyses?

## Deliverables

- FASTA length and GC summaries;
- FASTQ read-length and Phred-quality summaries;
- VCF record and variant-type summaries;
- a DNA reverse-complement utility;
- reproducible input preparation;
- standard-library tests;
- interpretation and limitation notes.

## Design choices

The programs use simple Python and small functions so that their behaviour can be inspected directly. Real inputs are retained, but large FASTQ files are subsetted to keep the repository lightweight. The outputs are deliberately descriptive and do not claim to replace full quality-control or variant-analysis software.

## Boundaries

The project focuses on format parsing and summary calculations. It does not implement full specification coverage, high-performance streaming or biological validation.

## Next extensions

Useful additions would include gzip input, the full IUPAC nucleotide alphabet, stronger malformed-record reporting, unit tests for edge cases and packaging the utilities as installable console commands.
