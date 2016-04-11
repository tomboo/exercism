import re


def abbreviate(phrase):
    regex = '[A-Z]+[a-z]*|[a-z]+'
    return ''.join(word[0].upper() for word in re.findall(regex, phrase))


if __name__ == '__main__':
    print(abbreviate('HyperText Markup language'))
