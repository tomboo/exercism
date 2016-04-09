def detect_anagrams(word, candidates):
    return [candidate
            for candidate in candidates
            if _letters(candidate) == _letters(word)
            if candidate.lower() != word.lower()]


def _letters(word):
    return sorted(word.lower())


if __name__ == '__main__':
    print(detect_anagrams('ant', 'tan stand at'.split()))
