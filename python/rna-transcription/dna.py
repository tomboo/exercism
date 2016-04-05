# -*- coding: utf-8 -*-
"""Solution to exercism:python/rna-transcription."""


def to_rna(dna_sequence):
    """
    Transcribe a sequence of DNA nucleotides to RNA nucleotides.

    Parameters
    ----------
    dna_sequence : str
        A sequence of characters in ('A', 'C', 'G', 'T') representing
        the DNA sequence.

    Returns
    -------
    rna_sequence : str
        The RNA sequence transcribed from dna_sequence.

    Notes
    -----
    DNA-RNA transcription algorithm:
        `G` -> `C`,  `C` -> `G`, `T` -> `A`, `A` -> `U`
    All characters in dna_sequence must be in [GgCcTtAa], else KeyError.

    Examples
    --------
    >>> to_rna('GCTA')
    'CGAU'
    >>> to_rna('atcg')
    'UAGC'
    """
    # Create a dictionary to look up RNA characters
    dna_to_rna = {
        'A': 'U',
        'C': 'G',
        'G': 'C',
        'T': 'A',
        }

    return ''.join(dna_to_rna[c] for c in dna_sequence.upper())
