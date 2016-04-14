_plants = {
    'C': 'Clover',
    'G': 'Grass',
    'R': 'Radishes',
    'V': 'Violets'
    }

_children = [
    'Alice', 'Bob', 'Charlie', 'David',
    'Eve', 'Fred', 'Ginny', 'Harriet',
    'Ileana', 'Joseph', 'Kincaid', 'Larry'
    ]


class Garden():
    def __init__(self, garden, students=_children):
        self.rows = garden.split()
        self.students = sorted(students)

    def plants(self, child):
        i = self.students.index(child) * 2
        j = i + 2
        p = self.rows[0][i:j] + self.rows[1][i:j]
        return [_plants[c] for c in p]


if __name__ == '__main__':
    garden = Garden("VVCCGG\nVVCCGG")
    print(garden.plants("Bob"))
