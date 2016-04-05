# -*- coding: utf-8 -*-
import string


def is_pangram(s):
    return not set(string.ascii_lowercase) - set(s.lower())
