import unittest
from pathFinder.helpers import *


class HelpersTests(unittest.TestCase):
    def test_next_movement(self):
        combinations = set()
        combinations.add("B3")
        combinations.add("C2")
        self.assertSetEqual(combinations, calculate_next_movements("A1"))

        combinations = set()
        combinations.add("A4")
        combinations.add("C4")
        combinations.add("D3")
        combinations.add("D1")
        self.assertSetEqual(combinations, calculate_next_movements("B2"))

        combinations = set()
        combinations.add("E7")
        combinations.add("G7")
        combinations.add("H6")
        combinations.add("H4")
        combinations.add("G3")
        combinations.add("E3")
        combinations.add("D4")
        combinations.add("D6")
        self.assertSetEqual(combinations, calculate_next_movements("F5"))

    def test_letter_to_number(self):
        self.assertEqual(1, letter_to_number("A"))
        self.assertEqual(2, letter_to_number("B"))
        self.assertEqual(3, letter_to_number("C"))
        self.assertEqual(4, letter_to_number("D"))
        self.assertEqual(5, letter_to_number("E"))
        self.assertEqual(6, letter_to_number("F"))
        self.assertEqual(7, letter_to_number("G"))
        self.assertEqual(8, letter_to_number("H"))

    def test_number_to_letter(self):
        self.assertEqual("A", number_to_letter(1))
        self.assertEqual("B", number_to_letter(2))
        self.assertEqual("C", number_to_letter(3))
        self.assertEqual("D", number_to_letter(4))
        self.assertEqual("E", number_to_letter(5))
        self.assertEqual("F", number_to_letter(6))
        self.assertEqual("G", number_to_letter(7))
        self.assertEqual("H", number_to_letter(8))