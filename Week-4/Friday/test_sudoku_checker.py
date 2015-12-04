import sudoku_checker
import unittest

class TestSudokuChecker(unittest.TestCase):
    def test_is_complete_empty(self):
        test_input = []
        expected = False
        actual = sudoku_checker.is_complete(test_input)
        self.assertEqual(expected, actual, "The row is empty.")

    def test_is_complete_too_short(self):
        test_input = [1, 2, 3, 4, 5, 6, 7, 8]
        expected = False
        actual = sudoku_checker.is_complete(test_input)
        self.assertEqual(expected, actual, "The row is too short.")

    def test_is_complete_too_long(self):
        test_input = [1, 2, 3, 4, 5, 6, 6, 7, 8, 8, 9]
        expected = False
        actual = sudoku_checker.is_complete(test_input)
        self.assertEqual(expected, actual, "The row is too long")

    def test_is_complete_nine_element(self):
        test_input = [1, 2, 3, 4, 4, 4, 7, 7, 7]
        expected = True
        actual = sudoku_checker.is_complete(test_input)
        self.assertEqual(expected, actual, "The row has not nine elements" )

    def test_integer_checking_negative(self):
        test_input = [1, 2, -3, -4, 5, 6]
        expected = False
        actual = sudoku_checker.integer_checking(test_input)
        self.assertEqual(expected, actual, "It has negative elements")

    def test_integer_checking_above_nine(self):
        test_input = [1, 2, 11, 23]
        expected = False
        actual = sudoku_checker.integer_checking(test_input)
        self.assertEqual(expected, actual, "It has too large elements")

unittest.main()
