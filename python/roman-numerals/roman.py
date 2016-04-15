_alphabet = (
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I')
    )


def numeral(number):
    s = ''
    for arabic, roman in _alphabet:
        while number >= arabic:
            s += roman
            number -= arabic
    return s


if __name__ == '__main__':
    print(numeral(4))
