_vocab = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three',
    4: 'four', 5: 'five', 6: 'six', 7: 'seven',
    8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
    12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
    16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
    20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
    60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety',
    100: 'hundred', 1e3: 'thousand', 1e6: 'million', 1e9: 'billion'
    }


def phrase(n, flag=False):
    if n < 20:
        result = []
        if flag:
            result += ['and']
        return result + [_vocab[n]]
    if n < 100:
        s = _vocab[(n // 10) * 10]
        if n % 10:
            s += '-' + _vocab[n % 10]
        return [s]
    if n < 1000:
        result = [_vocab[n // 100]] + [_vocab[100]]
        if n % 100 != 0:
            result += ['and'] + phrase(n % 100)
        return result
    if n < 1e6:
        result = phrase(n // 1e3) + [_vocab[1e3]]
        if n % 1e3:
            result += phrase(n % 1e3, True)
        return result
    if n < 1e9:
        result = phrase(n // 1e6) + [_vocab[1e6]]
        if n % 1e6:
            result += phrase(n % 1e6, True)
        return result
    if n < 1e12:
        result = phrase(n // 1e9) + [_vocab[1e9]]
        if n % 1e9:
            result += phrase(n % 1e9, True)
        return result


def say(n):
    if n < 0:
        raise AttributeError('number is negative')
    if n >= 1e12:
        raise AttributeError('number is too large: %s' % str(n))

    return ' '.join(phrase(n))


if __name__ == '__main__':
    print(say(1029))
