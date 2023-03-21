from enum import Enum
from io import StringIO
from unittest import TestCase
from unittest.mock import patch

import gradebook


class TestPerson(TestCase):
    def test_update_first_name(self):
        test_case = [
            'Adam',
            'Mark',
            'Mike'
        ]
        for (expected) in test_case:
            with self.subTest(f'{expected}'):
                p = gradebook.Student()
                p.update_first_name(expected)
                self.assertEqual(expected, p.first_name)

    def test_update_last_name(self):
        test_case = [
            'Barto',
            'Lucas',
            'Smith'
        ]
        for (expected) in test_case:
            with self.subTest(f'{expected}'):
                p = gradebook.Instructor()
                p.update_last_name(expected)
                self.assertEqual(expected, p.last_name)

    def test_update_dob(self):  # Make this a Date Value
        test_case = [
            'Barto',
            'Lucas',
            'Smith'
        ]
        for (expected) in test_case:
            with self.subTest(f'{expected}'):
                p = gradebook.ZipCodeStudent()
                p.update_dob(expected)
                self.assertEqual(expected, p.dob)

    def test_update_status(self):  # this will return anything I give it as correct... Fix this?
        class AliveStatus(Enum):
            Deceased = 0
            Alive = 1

        test_case = [
            AliveStatus.Alive,
            AliveStatus.Alive,
            AliveStatus.Deceased
        ]
        for (expected) in test_case:
            with self.subTest(f'{expected}'):
                p = gradebook.College()
                p.update_status(expected)
                self.assertEqual(expected, p.status)

    def test_add_instructor(self):
        test_case = [
            ([gradebook.Instructor, gradebook.Instructor], 2),
        ]
        for (peoples, expected) in test_case:
            with self.subTest(f'{peoples}, {expected}'):
                room = gradebook.Classroom()
                for people in peoples:
                    room.add_instructor(people)
                self.assertEqual(expected, len(room.instructors))

    def test_remove_instructor(self):
        room = gradebook.Classroom()
        instructor = gradebook.Instructor()
        room.add_instructor(instructor)
        room.remove_instructor(instructor)
        expected = []
        actual = room.instructors
        self.assertEqual(expected, actual)

    def test_add_student(self):
        test_case = [
            ([gradebook.Student, gradebook.Student], 2),
        ]
        for (peoples, expected) in test_case:
            with self.subTest(f'{peoples}, {expected}'):
                room = gradebook.Classroom()
                for people in peoples:
                    room.add_student(people)
                self.assertEqual(expected, len(room.students))

    def test_remove_student(self):
        room = gradebook.Classroom()
        student = gradebook.Student()
        room.add_student(student)
        room.remove_student(student)
        expected = []
        actual = room.students
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_instructors(self, mock_stdout):
        test_case = [
            ([gradebook.Instructor, gradebook.Instructor], "[<class 'gradebook.Instructor'>, <class 'gradebook.Instructor'>]\n"),
        ]
        for (peoples, expected) in test_case:
            with self.subTest(f'{peoples}, {expected}'):
                room = gradebook.Classroom()
                for people in peoples:
                    room.add_instructor(people)
                room.print_instructors()
                self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_students(self, mock_stdout):
        test_case = [
            ([gradebook.Student, gradebook.Student], "[<class 'gradebook.Student'>, <class 'gradebook.Student'>]\n"),
        ]
        for (peoples, expected) in test_case:
            with self.subTest(f'{peoples}, {expected}'):
                room = gradebook.Classroom()
                for people in peoples:
                    room.add_student(people)
                room.print_students()
                self.assertEqual(expected, mock_stdout.getvalue())
