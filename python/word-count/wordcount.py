# -*- coding: utf-8 -*-
import re


def word_count(line):
    print(line)
    words = re.split(r'[\s\t\n]+', line)
    for word in words:
        print(word)
    return 0

if __name__ == '__main__':
    print(word_count(' one two three'))
