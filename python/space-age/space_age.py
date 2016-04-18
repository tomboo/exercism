class SpaceAge():
    def __init__(self, seconds):
        self.seconds = seconds

    def converter(self, f):
        return round(self.seconds / f, 2)

    def on_earth(self):
        return self.converter(1.0 * 31557600)

    def on_mercury(self):
        return self.converter(0.2408467 * 31557600)

    def on_venus(self):
        return self.converter(0.61519726 * 31557600)

    def on_mars(self):
        return self.converter(1.8808158 * 31557600)

    def on_jupiter(self):
        return self.converter(11.862615 * 31557600)

    def on_saturn(self):
        return self.converter(29.447498 * 31557600)

    def on_uranus(self):
        return self.converter(84.016846 * 31557600)

    def on_neptune(self):
        return self.converter(164.79132 * 31557600)


if __name__ == '__main__':
    age = SpaceAge(3e9)
    print(age.seconds)
    print(age.on_earth())
    print(age.on_saturn())
