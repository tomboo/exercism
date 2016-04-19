class Luhn():
    def __init__(self, number):
        self.number = number

    def addends(self):
        return []

    def checksum(self):
        return 0

    def is_valid(self):
        return True

    @staticmethod
    def create(base):
        return 0


if __name__ == '__main__':
    number = Luhn(8631)
    print(number.addends())
