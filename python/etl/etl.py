def transform(old):
    return {
        letter.lower(): points
        for points, letters in old.items()
        for letter in letters
    }


if __name__ == '__main__':
    old = {1: ['WORLD', 'GSCHOOLERS']}
    expected = {'world': 1, 'gschoolers': 1}
    print(transform(old))
