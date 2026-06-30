#!/usr/bin/env python3

"""
Simple standard-library test runner for the bioinformatics utilities.
"""

import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def run_command(command):
    result = subprocess.run(
        command,
        cwd=PROJECT_ROOT,
        text=True,
        capture_output=True
    )

    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr)
        raise AssertionError(f"Command failed: {' '.join(command)}")

    return result.stdout


def assert_contains(text, expected):
    if expected not in text:
        raise AssertionError(f"Expected '{expected}' in output:\n{text}")


def test_fasta_stats():
    output = run_command([
        sys.executable,
        "src/fasta_stats.py",
        "data/inputs/reference/ecoli_rel606_reference.fasta"
    ])
    assert_contains(output, "sequence_count:")
    assert_contains(output, "total_length:")
    assert_contains(output, "gc_percent:")


def test_fastq_basic_qc():
    output = run_command([
        sys.executable,
        "src/fastq_basic_qc.py",
        "data/inputs/reads/SRR2584866_R1_1000_reads.fastq"
    ])
    assert_contains(output, "read_count: 1000")
    assert_contains(output, "total_bases:")


def test_vcf_summary():
    output = run_command([
        sys.executable,
        "src/vcf_summary.py",
        "data/inputs/variants/SRR2584866_filtered_variants.vcf"
    ])
    assert_contains(output, "total_variants: 407")
    assert_contains(output, "SNP: 353")
    assert_contains(output, "indel_or_complex: 54")


def test_reverse_complement():
    output = run_command([
        sys.executable,
        "src/reverse_complement.py",
        "ATGCCGTA"
    ])
    assert output.strip() == "TACGGCAT"


def main():
    tests = [
        test_fasta_stats,
        test_fastq_basic_qc,
        test_vcf_summary,
        test_reverse_complement,
    ]

    for test in tests:
        test()
        print(f"PASS: {test.__name__}")

    print("All tests passed.")


if __name__ == "__main__":
    main()
