def hey(what):
    ws = what.strip()
    if not ws:
        return 'Fine. Be that way!'
    elif ws.isupper():
        return 'Whoa, chill out!'
    elif ws[-1] == '?':
        return 'Sure.'
    else:
        return 'Whatever.'


if __name__ == '__main__':
    print(hey('4?'))
