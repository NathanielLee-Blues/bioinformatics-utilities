# Interpretation

## Summary

This project demonstrates a small set of Python utilities for common bioinformatics file formats.

The tools were tested using real input files from an E. coli variant-calling workflow: a reference FASTA, paired-end FASTQ read subsets, and a filtered VCF.

## FASTA statistics interpretation

The FASTA utility found one reference sequence with a total length of 4,629,812 bases and GC content of 50.77%.

This is consistent with summarising a single bacterial reference genome sequence.

## FASTQ QC interpretation

The FASTQ utility summarised 1,000 reads from each paired-end read file.

For R1, the mean read length was 127.43 bases and the mean Phred quality score was 35.22.

For R2, the mean read length was 131.41 bases and the mean Phred quality score was 35.55.

These values suggest that the subsetted reads are generally high quality, although this simple script does not replace full tools such as FastQC or MultiQC.

## VCF summary interpretation

The VCF utility identified 407 filtered candidate variants.

These included:

- 353 SNPs
- 54 indel or complex variants

All variants were located on contig `CP000819.1`.

This matches the output from the earlier variant-calling workflow and shows that the utility can parse and summarise real VCF data.

## Reverse complement interpretation

The reverse-complement utility correctly converted:

    ATGCCGTA

to:

    TACGGCAT

This demonstrates simple sequence manipulation using standard DNA base-pairing rules.

## Overall conclusion

This project demonstrates practical Python scripting for bioinformatics file handling. It provides evidence of command-line tool design, parsing of common genomics file formats, structured CSV output, and basic testing.
