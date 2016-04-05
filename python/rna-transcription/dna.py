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


def to_rna(s):
    t = ''
    for c in s:
        if c == 'G':
            t += 'C'
        elif c == 'C':
            t += 'G'
        elif c == 'T':
            t += 'A'
        elif c == 'A':
            t += 'U'
    return t


if __name__ == '__main__':
    print(to_rna('ACGTGGTCTTAA'))  # 'UGCACCAGAAUU'
