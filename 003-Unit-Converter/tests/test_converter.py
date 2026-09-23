"""
test_converter.py

Unit tests untuk fungsi konversi Unit Converter CLI.
Task 003 - Unit Converter CLI
"""

import unittest

from src.converter import (
    convert_length,
    convert_storage,
    convert_temperature,
    convert_time,
    convert_weight,
)


class TestLengthConversion(unittest.TestCase):
    """Test konversi panjang."""

    def test_meter_to_kilometer(self) -> None:
        self.assertEqual(convert_length(1000, "m", "km"), 1.0)

    def test_kilometer_to_meter(self) -> None:
        self.assertEqual(convert_length(2, "km", "m"), 2000.0)

    def test_centimeter_to_meter(self) -> None:
        self.assertEqual(convert_length(100, "cm", "m"), 1.0)

    def test_millimeter_to_centimeter(self) -> None:
        self.assertEqual(convert_length(10, "mm", "cm"), 1.0)

    def test_same_unit(self) -> None:
        self.assertEqual(convert_length(25, "m", "m"), 25.0)


class TestWeightConversion(unittest.TestCase):
    """Test konversi berat."""

    def test_gram_to_kilogram(self) -> None:
        self.assertEqual(convert_weight(1000, "g", "kg"), 1.0)

    def test_kilogram_to_gram(self) -> None:
        self.assertEqual(convert_weight(2, "kg", "g"), 2000.0)

    def test_milligram_to_gram(self) -> None:
        self.assertEqual(convert_weight(1000, "mg", "g"), 1.0)

    def test_ton_to_kilogram(self) -> None:
        self.assertEqual(convert_weight(1, "ton", "kg"), 1000.0)

    def test_same_unit(self) -> None:
        self.assertEqual(convert_weight(25, "kg", "kg"), 25.0)


class TestTimeConversion(unittest.TestCase):
    """Test konversi waktu."""

    def test_second_to_minute(self) -> None:
        self.assertEqual(convert_time(60, "detik", "menit"), 1.0)

    def test_minute_to_hour(self) -> None:
        self.assertEqual(convert_time(60, "menit", "jam"), 1.0)

    def test_hour_to_day(self) -> None:
        self.assertEqual(convert_time(24, "jam", "hari"), 1.0)

    def test_day_to_second(self) -> None:
        self.assertEqual(convert_time(1, "hari", "detik"), 86400.0)

    def test_same_unit(self) -> None:
        self.assertEqual(convert_time(25, "jam", "jam"), 25.0)


class TestTemperatureConversion(unittest.TestCase):
    """Test konversi suhu."""

    def test_celsius_to_fahrenheit(self) -> None:
        self.assertAlmostEqual(
            convert_temperature(0, "C", "F"),
            32.0,
        )

    def test_fahrenheit_to_celsius(self) -> None:
        self.assertAlmostEqual(
            convert_temperature(32, "F", "C"),
            0.0,
        )

    def test_celsius_to_kelvin(self) -> None:
        self.assertAlmostEqual(
            convert_temperature(0, "C", "K"),
            273.15,
        )

    def test_kelvin_to_celsius(self) -> None:
        self.assertAlmostEqual(
            convert_temperature(273.15, "K", "C"),
            0.0,
        )

    def test_fahrenheit_to_kelvin(self) -> None:
        self.assertAlmostEqual(
            convert_temperature(32, "F", "K"),
            273.15,
        )

    def test_kelvin_to_fahrenheit(self) -> None:
        self.assertAlmostEqual(
            convert_temperature(273.15, "K", "F"),
            32.0,
        )

    def test_same_unit(self) -> None:
        self.assertEqual(
            convert_temperature(25, "C", "C"),
            25,
        )

    def test_invalid_temperature_conversion(self) -> None:
        with self.assertRaises(ValueError):
            convert_temperature(100, "C", "X")


class TestStorageConversion(unittest.TestCase):
    """Test konversi penyimpanan."""

    def test_byte_to_kilobyte(self) -> None:
        self.assertEqual(convert_storage(1024, "B", "KB"), 1.0)

    def test_kilobyte_to_megabyte(self) -> None:
        self.assertEqual(convert_storage(1024, "KB", "MB"), 1.0)

    def test_megabyte_to_gigabyte(self) -> None:
        self.assertEqual(convert_storage(1024, "MB", "GB"), 1.0)

    def test_gigabyte_to_terabyte(self) -> None:
        self.assertEqual(convert_storage(1024, "GB", "TB"), 1.0)

    def test_terabyte_to_byte(self) -> None:
        self.assertEqual(
            convert_storage(1, "TB", "B"),
            1024 ** 4,
        )

    def test_same_unit(self) -> None:
        self.assertEqual(
            convert_storage(25, "MB", "MB"),
            25.0,
        )


class TestDecimalConversion(unittest.TestCase):
    """Test nilai desimal."""

    def test_decimal_length(self) -> None:
        self.assertAlmostEqual(
            convert_length(1.5, "m", "cm"),
            150.0,
        )

    def test_decimal_weight(self) -> None:
        self.assertAlmostEqual(
            convert_weight(2.5, "kg", "g"),
            2500.0,
        )

    def test_decimal_time(self) -> None:
        self.assertAlmostEqual(
            convert_time(1.5, "jam", "menit"),
            90.0,
        )

    def test_decimal_storage(self) -> None:
        self.assertAlmostEqual(
            convert_storage(1.5, "GB", "MB"),
            1536.0,
        )


class TestNegativeValues(unittest.TestCase):
    """Test nilai negatif yang valid secara matematis."""

    def test_negative_length(self) -> None:
        self.assertEqual(
            convert_length(-1, "m", "cm"),
            -100.0,
        )

    def test_negative_temperature(self) -> None:
        self.assertAlmostEqual(
            convert_temperature(-40, "C", "F"),
            -40.0,
        )

    def test_negative_weight(self) -> None:
        self.assertEqual(
            convert_weight(-2, "kg", "g"),
            -2000.0,
        )


if __name__ == "__main__":
    unittest.main()
