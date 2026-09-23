"""
validator.py

Berisi fungsi validasi input untuk Unit Converter CLI.
Task 003 - Unit Converter CLI
"""

from __future__ import annotations


CATEGORY_UNITS: dict[str, tuple[str, ...]] = {
    "panjang": (
        "mm",
        "cm",
        "m",
        "km",
    ),
    "berat": (
        "mg",
        "g",
        "kg",
        "ton",
    ),
    "waktu": (
        "detik",
        "menit",
        "jam",
        "hari",
    ),
    "suhu": (
        "C",
        "F",
        "K",
    ),
    "penyimpanan": (
        "B",
        "KB",
        "MB",
        "GB",
        "TB",
    ),
}


def normalize_category(category: str) -> str:
    """
    Menormalisasi nama kategori.

    Contoh:
        "Panjang" -> "panjang"
        " PANJANG " -> "panjang"
    """
    if not isinstance(category, str):
        raise TypeError("Kategori harus berupa teks.")

    normalized = category.strip().lower()

    if not normalized:
        raise ValueError("Kategori tidak boleh kosong.")

    return normalized


def validate_category(category: str) -> str:
    """
    Memvalidasi kategori konversi.

    Mengembalikan kategori dalam bentuk lowercase.
    """
    normalized = normalize_category(category)

    if normalized not in CATEGORY_UNITS:
        available = ", ".join(CATEGORY_UNITS.keys())
        raise ValueError(
            f"Kategori tidak valid: {category!r}. "
            f"Pilihan: {available}."
        )

    return normalized


def get_units(category: str) -> tuple[str, ...]:
    """
    Mengembalikan daftar unit yang tersedia untuk kategori tertentu.
    """
    normalized = validate_category(category)
    return CATEGORY_UNITS[normalized]


def validate_unit(category: str, unit: str) -> str:
    """
    Memvalidasi unit berdasarkan kategori.

    Unit suhu bersifat case-sensitive:
        C, F, K

    Unit lainnya mengikuti bentuk yang didefinisikan
    pada CATEGORY_UNITS.
    """
    if not isinstance(unit, str):
        raise TypeError("Unit harus berupa teks.")

    normalized_category = validate_category(category)
    normalized_unit = unit.strip()

    if not normalized_unit:
        raise ValueError("Unit tidak boleh kosong.")

    available_units = CATEGORY_UNITS[normalized_category]

    if normalized_unit not in available_units:
        available = ", ".join(available_units)
        raise ValueError(
            f"Unit tidak valid: {unit!r}. "
            f"Untuk kategori {normalized_category!r}, "
            f"pilihan: {available}."
        )

    return normalized_unit


def validate_number(value: str | int | float) -> float:
    """
    Memvalidasi dan mengubah nilai menjadi float.

    Menerima:
        "10"
        "10.5"
        10
        10.5
        -5

    Menolak:
        string kosong
        teks biasa
        NaN
        infinity
    """
    if isinstance(value, bool):
        raise TypeError("Nilai boolean tidak valid sebagai angka.")

    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(
            f"Nilai harus berupa angka: {value!r}."
        ) from exc

    if not __import__("math").isfinite(number):
        raise ValueError(
            "Nilai harus berupa angka finite, bukan NaN atau infinity."
        )

    return number
