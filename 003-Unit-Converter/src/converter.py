"""
converter.py

Berisi seluruh fungsi konversi satuan.
Task 003 - Unit Converter CLI
"""

# =========================
# PANJANG
# Basis: meter
# =========================

LENGTH_FACTORS = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0,
}


# =========================
# BERAT
# Basis: gram
# =========================

WEIGHT_FACTORS = {
    "mg": 0.001,
    "g": 1.0,
    "kg": 1000.0,
    "ton": 1_000_000.0,
}


# =========================
# WAKTU
# Basis: detik
# =========================

TIME_FACTORS = {
    "detik": 1,
    "menit": 60,
    "jam": 3600,
    "hari": 86400,
}


# =========================
# PENYIMPANAN
# Basis: byte
# =========================

STORAGE_FACTORS = {
    "B": 1,
    "KB": 1024,
    "MB": 1024 ** 2,
    "GB": 1024 ** 3,
    "TB": 1024 ** 4,
}


def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    """Konversi panjang."""
    meter = value * LENGTH_FACTORS[from_unit]
    return meter / LENGTH_FACTORS[to_unit]


def convert_weight(value: float, from_unit: str, to_unit: str) -> float:
    """Konversi berat."""
    gram = value * WEIGHT_FACTORS[from_unit]
    return gram / WEIGHT_FACTORS[to_unit]


def convert_time(value: float, from_unit: str, to_unit: str) -> float:
    """Konversi waktu."""
    second = value * TIME_FACTORS[from_unit]
    return second / TIME_FACTORS[to_unit]


def convert_storage(value: float, from_unit: str, to_unit: str) -> float:
    """Konversi penyimpanan."""
    byte = value * STORAGE_FACTORS[from_unit]
    return byte / STORAGE_FACTORS[to_unit]


# =========================
# SUHU
# =========================

def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:

    if from_unit == to_unit:
        return value

    # Celsius
    if from_unit == "C":
        if to_unit == "F":
            return (value * 9 / 5) + 32

        if to_unit == "K":
            return value + 273.15

    # Fahrenheit
    if from_unit == "F":
        if to_unit == "C":
            return (value - 32) * 5 / 9

        if to_unit == "K":
            return ((value - 32) * 5 / 9) + 273.15

    # Kelvin
    if from_unit == "K":
        if to_unit == "C":
            return value - 273.15

        if to_unit == "F":
            return ((value - 273.15) * 9 / 5) + 32

    raise ValueError("Konversi suhu tidak didukung.")
