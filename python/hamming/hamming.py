def distance(s1, s2):
    assert(len(s1) == len(s2))
    return sum(a != b for a, b in zip(s1, s2))


if __name__ == '__main__':
    assert distance('AG', 'CT') == 2
