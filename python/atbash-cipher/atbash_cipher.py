from string import ascii_lowercase

trans_tab = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])


def clean(s):
    return ''.join(c for c in s if c.isalnum()).lower()


def encode(s):
    t = clean(s)
    t = t.translate(trans_tab)
    t = ' '.join(t[i:i + 5] for i in range(0, len(t), 5))
    return t


def decode(s):
    t = clean(s)
    t = t.translate(trans_tab)
    return t

if __name__ == '__main__':
    s = 'aBcDef 123456 +-*/.'
    print(clean(s))
    print(encode(s))
    print(decode(encode(s)))
