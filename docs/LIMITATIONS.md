# Limitations

## Performance and memory

The programs use straightforward Python parsing and are designed for small or moderate files. They are not optimised for whole-cohort VCFs, compressed streaming at scale or very large metagenomic FASTA and FASTQ datasets.

## Format coverage

Bioinformatics formats contain many optional fields and edge cases. The tools support the structures needed by the included inputs but do not attempt to implement every part of the FASTA, FASTQ or VCF specifications.

## FASTA summary

GC percentage and length statistics do not measure assembly completeness, contamination, gene content or structural correctness.

## FASTQ quality summary

A mean Phred score cannot show per-cycle deterioration, adapter sequence, duplication, overrepresented reads or quality distributions. The utility should complement, not replace, FastQC or MultiQC.

## VCF summary

Counting records and variant types does not validate genotype quality or biological truth. Multi-allelic records, normalisation, symbolic alleles and complex representations may need more specialised handling.

## Reverse complement

The sequence tool supports standard DNA bases and `N`. It does not currently support the complete IUPAC ambiguity alphabet, RNA-specific behaviour or FASTA-formatted multi-record input.

## Testing

The included tests cover expected values for the example data and core behaviour. They are not a comprehensive property-based or specification-level test suite.

## Dependency on another project

The preparation script expects inputs from the companion variant-calling workflow. Paths may need to be changed when the repositories are stored in a different layout.

## Practical implication

The programs are appropriate for transparent examples and quick checks. Dedicated tools or mature libraries should be used when correctness across diverse files, performance or production support is required.
