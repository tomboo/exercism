from collections import defaultdict


class School(object):
    def __init__(self, name):
        self.name = name
        self.db = defaultdict(set)

    def add(self, student, grade):
        '''Add a student's name to the roster for a grade'''
        self.db[grade].add(student)

    def grade(self, level):
        '''Get a list of all students enrolled in a grade'''
        return self.db[level]

    def sort(self):
        '''Get a sorted list of all students in all grades'''
        return sorted((grade, tuple(sorted(students)))
                      for grade, students in self.db.items())


if __name__ == '__main__':
    school = School("Haleakala Hippy School")
    school.add('Annie', 2)
    school.add('Frank', 2)
    school.add('Ken', 3)
    print(school.grade(2))
    print(school.sort())
