NORTH, EAST, SOUTH, WEST = range(4)


class Robot():
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.x = x
        self.y = y

    def advance(self):
        if self.bearing == NORTH:
            self.y += 1
        elif self.bearing == EAST:
            self.x += 1
        elif self.bearing == SOUTH:
            self.y -= 1
        elif self.bearing == WEST:
            self.x -= 1

    def turn_right(self):
        self.bearing = (self.bearing + 1) % 4

    def turn_left(self):
        self.bearing = (self.bearing - 1) % 4

    def simulate(self, program):
        step = {'A': self.advance,
                'R': self.turn_right,
                'L': self.turn_left
                }
        for s in program:
            step[s]()

    @property
    def coordinates(self):
        return (self.x, self.y)


if __name__ == '__main__':
    robot = Robot()
    robot.simulate('LAAARALA')
    print(robot.bearing, robot.coordinates)
