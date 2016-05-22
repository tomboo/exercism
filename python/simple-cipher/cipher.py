class Caesar():
    def encode(self, s):
        t = ''
        for c in s:
            print(ord(c))
            t += chr((ord(c) + 3) % 26)
        return t

    def decode(self, s):
        return s


class Cipher():
    pass


if __name__ == '__main__':
    print(Caesar().encode('abc'))
