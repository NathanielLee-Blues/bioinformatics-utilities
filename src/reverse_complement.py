#!/usr/bin/env python3

"""
Generate the reverse complement of a DNA sequence.
"""

import argparse


COMPLEMENT = str.maketrans({
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G",
    "N": "N",
    "a": "t",
    "t": "a",
    "g": "c",
    "c": "g",
    "n": "n",
})


def reverse_complement(sequence):
    return sequence.translate(COMPLEMENT)[::-1].upper()


def main():
    parser = argparse.ArgumentParser(description="Generate the reverse complement of a DNA sequence.")
    parser.add_argument("sequence", help="DNA sequence")
    args = parser.parse_args()

    print(reverse_complement(args.sequence))


if __name__ == "__main__":
    main()
