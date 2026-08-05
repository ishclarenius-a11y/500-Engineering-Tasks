"""
test_calculator.py

Unit test untuk calculator.py
"""

import unittest

from src.calculator import (
    tambah,
    kurang,
    kali,
    bagi,
    pangkat,
    modulus,
)


class TestCalculator(unittest.TestCase):

    def test_tambah(self):
        self.assertEqual(tambah(10, 20), 30)
        self.assertEqual(tambah(-5, 2), -3)

    def test_kurang(self):
        self.assertEqual(kurang(20, 5), 15)
        self.assertEqual(kurang(5, 20), -15)

    def test_kali(self):
        self.assertEqual(kali(5, 6), 30)
        self.assertEqual(kali(-2, 8), -16)

    def test_bagi(self):
        self.assertEqual(bagi(20, 5), 4)
        self.assertAlmostEqual(bagi(5, 2), 2.5)

    def test_bagi_nol(self):
        with self.assertRaises(ZeroDivisionError):
            bagi(10, 0)

    def test_pangkat(self):
        self.assertEqual(pangkat(2, 10), 1024)
        self.assertEqual(pangkat(5, 2), 25)

    def test_modulus(self):
        self.assertEqual(modulus(10, 3), 1)
        self.assertEqual(modulus(20, 5), 0)

    def test_modulus_nol(self):
        with self.assertRaises(ZeroDivisionError):
            modulus(10, 0)


if __name__ == "__main__":
    unittest.main()
