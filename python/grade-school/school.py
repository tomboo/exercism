class School():
    def __init__(self, name):
        self.name = name
        self.roster = {}

    def add(self, student, grade):
        '''Add a student's name to the roster for a grade'''
        if grade not in self.roster.keys():
            self.roster[grade] = []
        self.roster[grade] += [student]

    def grade(self, grade):
        '''Get a list of all students enrolled in a grade'''
        if grade not in self.roster.keys():
            return []
        return self.roster[grade]

    def sort(self):
        '''Get a sorted list of all students in all grades'''
        grades = sorted(self.roster.keys())
        return [grade for grade in grades]


if __name__ == '__main__':
    school = School("Haleakala Hippy School")
    school.add('Annie', 2)
    school.add('Frank', 2)
    print(school.grade(2))
    print(school.sort())
