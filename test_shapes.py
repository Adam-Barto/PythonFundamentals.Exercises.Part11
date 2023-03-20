from unittest import TestCase
import shapes

class TestShapes(TestCase):
    def test_area_rectangle(self):
        test_cases = {
            (5, 2, 10),
            (10, 30, 300),
            (2, 4, 8)
        }
        for length, width, actual in test_cases:
            with self.subTest(f'{length}, {width}, {actual}'):
                rectangle = shapes.Rectangle(length, width)
                self.assertEqual(actual, rectangle.area())


    def test_perimeter_rectangle(self):
        test_cases = {
            (5, 2, 14),
            (10, 30, 80),
            (2, 42, 88)
        }
        for length, width, actual in test_cases:
            with self.subTest(f'{length}, {width}, {actual}'):
                rectangle = shapes.Rectangle(length, width)
                self.assertEqual(actual, rectangle.perimeter())
    def test_area_square(self):
        test_cases = {
            (8, 32),
            (30, 120),
            (21, 84)
        }
        for length_width, actual in test_cases:
            with self.subTest(f'{length_width}, {actual}'):
                square = shapes.Square(length_width)
                self.assertEqual(actual, square.perimeter())


    def test_perimeter_square(self):
        test_cases = {
            (8, 32),
            (30, 120),
            (21, 84)
        }
        for length_width, actual in test_cases:
            with self.subTest(f'{length_width}, {actual}'):
                square = shapes.Square(length_width)
                self.assertEqual(actual, square.perimeter())