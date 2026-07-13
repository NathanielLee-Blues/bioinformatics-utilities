# Methods

## Input preparation

`scripts/prepare_inputs.sh` copies the REL606 reference FASTA and filtered VCF from the companion variant-calling project. It also creates FASTQ subsets containing the first 1,000 reads from each paired-end file so that the repository remains small while retaining real sequencing records.

## FASTA parsing

`fasta_stats.py` identifies header lines, concatenates sequence lines for each record and calculates sequence count, total length, minimum, maximum and mean length, and GC percentage. Results are printed and can be written to CSV.

## FASTQ parsing

`fastq_basic_qc.py` reads FASTQ records in four-line units, validates the sequence and quality lengths, converts ASCII quality characters to Phred scores and calculates read-count, base-count, read-length and mean-quality summaries.

## VCF parsing

`vcf_summary.py` skips metadata lines, reads variant records, checks the filter field and classifies records as SNPs or indel/complex variants from the reference and alternate allele lengths. It also counts records by chromosome or contig.

## Reverse complement

`reverse_complement.py` validates the input DNA alphabet, maps each base to its complement and reverses the resulting sequence.

## Testing

`tests/run_tests.py` uses Python’s standard library to run the command-line programs and compare their results with expected values from the included data. This tests both the core calculations and the interfaces used by a user.

## Execution

No external Python package is required for the current programs. Run them with Python 3 from the repository root and use `-o` where a CSV output is required.
