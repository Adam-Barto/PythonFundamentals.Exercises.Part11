from enum import Enum
from unittest import TestCase

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

    def test_update_dob(self): # Make this a Date Value
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

    def test_update_status(self): # this will return anything I give it as correct... Fix this?
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
