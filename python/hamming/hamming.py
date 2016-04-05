# -*- coding: utf-8 -*-


def distance(s1, s2):
    '''
    Return the Hamming distance between two sequences of characters.
    '''
    assert(len(s1) == len(s2))

    return sum(s1[i] != s2[i] for i in range(len(s1)))
