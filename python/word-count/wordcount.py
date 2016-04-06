# -*- coding: utf-8 -*-
import re


def word_count(s):
    d = dict()
    l = re.split(r'[\W_]+', s.lower())
    for word in l:
        if word:
            # could use defaultdict instead
            d[word] = d.get(word, 0) + 1
    return d

if __name__ == '__main__':
    print(word_count(' no go Go go_go '))
