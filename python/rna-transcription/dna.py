# -*- coding: utf-8 -*-
'''
The four nucleotides found in DNA are adenine (A), cytosine (C), guanine (G)
and thymine (T).

The four nucleotides found in RNA are adenine (A), cytosine (C), guanine (G)
and uracil (U).

Given a DNA strand, its transcribed RNA strand is formed by replacing each
nucleotide with its complement:

  G -> C
  C -> G
  T -> A
  A -> U
'''


def to_rna(dna):
    dna_to_rna = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}

    return "".join([dna_to_rna[c] for c in dna.upper()])


if __name__ == '__main__':
    print(to_rna('ACGTGGTCTTAA'))  # 'UGCACCAGAAUU'
