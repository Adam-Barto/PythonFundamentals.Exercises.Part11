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
                p = gradebook.Student(234)
                p.update_first_name(expected)
                self.assertEqual(expected, p.first_name)

    def test_update_last_name(self):
        self.fail()

    def test_update_dob(self):
        self.fail()

    def test_update_status(self):
        self.fail()
