def encode(s):
    r = ''
    f = 1
    for i in range(len(s)):
        c = s[i]
        cnext = s[i + 1] if i < len(s) - 1 else ''
        if c == cnext:
            f += 1
        else:
            if f == 1:
                r += c
            else:
                r += str(f)
                r += c
            f = 1
    return r


def decode(s):
    r = ''
    f = 0
    for c in s:
        if c.isdigit():
            f = 10 * f + int(c)
        else:
            if f == 0:
                r += c
            else:
                r += c * f
            f = 0
    return r


if __name__ == '__main__':
    print(encode('AABBBCCCCD'))
    print(decode('2A3B4CD12X'))
