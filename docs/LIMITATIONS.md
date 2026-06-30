# Limitations

This project is a lightweight educational toolkit rather than a production bioinformatics package.

Important limitations include:

- The utilities are designed for small to moderate files, not very large production-scale datasets.
- FASTA parsing is simple and does not handle every possible edge case.
- FASTQ QC is basic and does not replace FastQC or MultiQC.
- VCF parsing is simplified and does not fully model complex genotype fields, annotations, or multi-sample VCFs.
- Reverse-complement functionality supports standard DNA bases but not the full IUPAC ambiguity alphabet.
- The project does not currently provide installable Python package structure.
- Testing uses a simple standard-library test runner rather than pytest.

Future improvements could include:

- converting the utilities into an installable package
- adding argparse subcommands
- adding pytest tests
- adding support for compressed `.gz` files
- adding more detailed FASTQ quality summaries
- improving VCF parsing for multi-sample files
- adding Biopython-based alternatives
