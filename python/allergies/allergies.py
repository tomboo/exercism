class Allergies():
    _allergen = [
        "eggs",
        "peanuts",
        "shellfish",
        "strawberries",
        "tomatoes",
        "chocolate",
        "pollen",
        "cats"
    ]

    def __init__(self, score):
        self.score = score

    def is_allergic_to(self, allergen):
        return self.score & 1 << self._allergen.index(allergen)

    @property
    def lst(self):
        return [allergen for allergen in self._allergen
                if self.is_allergic_to(allergen)]


if __name__ == '__main__':
    allergies = Allergies(5)
    print(allergies.is_allergic_to("eggs"))
    print(allergies.is_allergic_to("shellfish"))
    print(allergies.is_allergic_to("peanuts"))
    print(allergies.lst)
