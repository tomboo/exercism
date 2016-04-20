class Luhn():
    def __init__(self, number):
        self.number = number

    def _transform(self, digit):
        n = 2 * digit
        return n if n < 10 else n - 9

    def addends(self):
        r = [int(c) for c in str(self.number)]
        for i in range(len(r)):
            j = -i - 1
            if j % 2 == 0:
                r[j] = self._transform(r[j])
        return r

    def checksum(self):
        return sum(self.addends())

    def is_valid(self):
        return self.checksum() % 10 == 0

    @staticmethod
    def create(n):
        diff = (10 - Luhn(n * 10).checksum()) % 10
        return 10 * n + diff

if __name__ == '__main__':
    number = Luhn(8631)
    print(number.addends())
    print(Luhn(4913).checksum())
