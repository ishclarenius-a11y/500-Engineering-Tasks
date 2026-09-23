"""
main.py

Entry point dan orchestration untuk Unit Converter CLI.
Task 003 - Unit Converter CLI
"""

from __future__ import annotations

from collections.abc import Callable

from src.converter import (
    convert_length,
    convert_storage,
    convert_temperature,
    convert_time,
    convert_weight,
)
from src.menu import (
    goodbye,
    header,
    length_menu,
    main_menu,
    show_error,
    show_result,
    storage_menu,
    temperature_menu,
    time_menu,
    weight_menu,
)
from src.validator import (
    get_units,
    validate_category,
    validate_number,
    validate_unit,
)


ConverterFunction = Callable[[float, str, str], float]


CONVERTERS: dict[str, ConverterFunction] = {
    "panjang": convert_length,
    "berat": convert_weight,
    "waktu": convert_time,
    "suhu": convert_temperature,
    "penyimpanan": convert_storage,
}


CATEGORY_MENUS: dict[str, Callable[[], None]] = {
    "panjang": length_menu,
    "berat": weight_menu,
    "waktu": time_menu,
    "suhu": temperature_menu,
    "penyimpanan": storage_menu,
}


MENU_TO_CATEGORY: dict[str, str] = {
    "1": "panjang",
    "2": "berat",
    "3": "waktu",
    "4": "suhu",
    "5": "penyimpanan",
}


def read_number() -> float:
    """Membaca dan memvalidasi nilai numerik dari pengguna."""
    while True:
        value = input("Masukkan nilai: ")

        try:
            return validate_number(value)
        except (TypeError, ValueError) as exc:
            show_error(str(exc))


def read_unit(category: str, label: str) -> str:
    """Membaca dan memvalidasi unit dari pengguna."""
    while True:
        unit = input(f"{label}: ")

        try:
            return validate_unit(category, unit)
        except (TypeError, ValueError) as exc:
            show_error(str(exc))


def run_conversion(category: str) -> None:
    """Menjalankan satu sesi konversi untuk sebuah kategori."""
    category = validate_category(category)

    menu_function = CATEGORY_MENUS[category]
    converter = CONVERTERS[category]

    menu_function()

    available_units = get_units(category)
    print(f"Unit tersedia: {', '.join(available_units)}")
    print()

    value = read_number()
    from_unit = read_unit(category, "Dari unit")
    to_unit = read_unit(category, "Ke unit")

    try:
        result = converter(value, from_unit, to_unit)
    except (KeyError, ValueError) as exc:
        show_error(str(exc))
        return

    show_result(
        value=value,
        from_unit=from_unit,
        to_unit=to_unit,
        result=result,
    )


def main() -> None:
    """Menjalankan aplikasi Unit Converter CLI."""
    header()

    while True:
        main_menu()

        try:
            choice = input("Pilih menu: ").strip()
        except (KeyboardInterrupt, EOFError):
            print()
            goodbye()
            break

        if choice == "0":
            goodbye()
            break

        category = MENU_TO_CATEGORY.get(choice)

        if category is None:
            show_error(
                "Pilihan menu tidak valid. "
                "Silakan pilih angka 0 sampai 5."
            )
            continue

        try:
            run_conversion(category)
        except (KeyboardInterrupt, EOFError):
            print()
            goodbye()
            break


if __name__ == "__main__":
    main()
