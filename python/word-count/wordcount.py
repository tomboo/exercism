# -*- coding: utf-8 -*-
import re
from collections import Counter


def word_count(text):
    count = Counter()
    for word in re.split(r'[\W_]+', text.lower()):
        if word:
            count.update([word])
    return dict(count)

if __name__ == '__main__':
    print(word_count(' no go Go go_go '))
