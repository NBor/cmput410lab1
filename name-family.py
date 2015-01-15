class Student(object):

    def __init__(self, name, family):
        self.course_marks = {}
        self.name = name
        self.family = family

    def add_course_mark(self, course, mark):
        self.course_marks[course] = mark

    def average(self):
        total = sum(self.course_marks.values())
        return total/float(len(self.course_marks))

if __name__ == '__main__':
    student = Student('John', 'Smith')
    student.add_course_mark('french', 2.0)
    student.add_course_mark('german', 3.0)
    student.add_course_mark('english', 4.0)
    print student.average()
