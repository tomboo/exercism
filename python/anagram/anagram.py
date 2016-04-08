def detect_anagrams(word, candidate_list):
    r = []
    wl = word.lower()
    ws = ''.join(sorted(wl))
    for candidate in candidate_list:
        cl = candidate.lower()
        if wl != cl:
            if ws == ''.join(sorted(cl)):
                r.append(candidate)

    return r


if __name__ == '__main__':
    print(detect_anagrams('ant', 'tan stand at'.split()))
