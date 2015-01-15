class Student(object):

    """ Class to model a student.

    Stores the student's first and last name as attributes. Also stores a
    dictionary of all the students courses and marks.

    """

    def __init__(self, name, family):
        """Function to calc average gpa.

        >>> student = Student('John', 'Smith')
        >>> student.name
        'John'
        >>> student.family
        'Smith'

        """
        self.course_marks = {}
        self.name = name
        self.family = family

    def add_course_mark(self, course, mark):
        """Function to calc average gpa.

        >>> student = Student('John', 'Smith')
        >>> student.add_course_mark('french', 2.0)
        >>> student.course_marks
        {'french': 2.0}

        """
        self.course_marks[course] = mark

    def average(self):
        """Function to calc average gpa.

        >>> student = Student('John', 'Smith')
        >>> student.add_course_mark('french', 2.0)
        >>> student.add_course_mark('german', 3.0)
        >>> student.add_course_mark('english', 4.0)
        >>> student.average()
        3.0
        """
        total = sum(self.course_marks.values())
        return total/float(len(self.course_marks))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
