"""
calculator.py

Berisi seluruh operasi matematika.
"""


def tambah(a: float, b: float) -> float:
    """Mengembalikan hasil penjumlahan."""
    return a + b


def kurang(a: float, b: float) -> float:
    """Mengembalikan hasil pengurangan."""
    return a - b


def kali(a: float, b: float) -> float:
    """Mengembalikan hasil perkalian."""
    return a * b


def bagi(a: float, b: float) -> float:
    """
    Mengembalikan hasil pembagian.

    Raises:
        ZeroDivisionError
    """
    if b == 0:
        raise ZeroDivisionError(
            "Pembagian dengan nol tidak diperbolehkan."
        )

    return a / b


def pangkat(a: float, b: float) -> float:
    """Mengembalikan hasil perpangkatan."""
    return a ** b


def modulus(a: float, b: float) -> float:
    """
    Mengembalikan sisa hasil bagi.

    Raises:
        ZeroDivisionError
    """
    if b == 0:
        raise ZeroDivisionError(
            "Modulus dengan nol tidak diperbolehkan."
        )

    return a % b
