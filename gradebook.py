import uuid
from enum import Enum


class AliveStatus(Enum):
    Deceased = 0
    Alive = 1


class Person:
    def __init__(self, first_name='John', last_name='Doe', dob='1/01/2000', status=AliveStatus.Deceased):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.status = status

    def update_first_name(self, first_name):
        self.first_name = first_name

    def update_last_name(self, last_name):
        self.last_name = last_name

    def update_dob(self, dob):
        self.dob = dob

    def update_status(self, status):
        self.status = status


class Instructor(Person):
    def __init__(self, instructor_id=None):
        super(Person).__init__()
        self.instructor_id = "Instructor_" + str(uuid.uuid4())


class Student(Person):
    def __init__(self, student_id=None):
        super(Person).__init__()
        self.student_id = "Student_" + str(uuid.uuid4())


class ZipCodeStudent(Student):
    pass


class College(Student):
    pass


class Classroom:
    def __init__(self):
        self.students = []
        self.instructors = []

    def add_instructor(self, instructor):
        self.instructors.append(instructor)

    def remove_instructor(self, instructor):
        self.instructors.remove(instructor)

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def print_instructors(self):
        print(self.instructors)

    def print_students(self):
        print(self.students)
