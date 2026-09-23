"""
menu.py

Berisi seluruh tampilan aplikasi Unit Converter CLI.
"""

APP_NAME = "Unit Converter CLI"
VERSION = "1.0.0"


def line() -> None:
    """Menampilkan garis pemisah."""
    print("=" * 50)


def header() -> None:
    """Menampilkan header aplikasi."""
    line()
    print(APP_NAME)
    print(f"Version : {VERSION}")
    line()


def main_menu() -> None:
    """Menampilkan menu utama."""
    print()
    print("===== MENU UTAMA =====")
    print("1. Panjang")
    print("2. Berat")
    print("3. Waktu")
    print("4. Suhu")
    print("5. Penyimpanan")
    print("0. Keluar")
    print()


def length_menu() -> None:
    """Daftar satuan panjang."""
    print()
    print("Satuan Panjang")
    print("- mm")
    print("- cm")
    print("- m")
    print("- km")
    print()


def weight_menu() -> None:
    """Daftar satuan berat."""
    print()
    print("Satuan Berat")
    print("- mg")
    print("- g")
    print("- kg")
    print("- ton")
    print()


def time_menu() -> None:
    """Daftar satuan waktu."""
    print()
    print("Satuan Waktu")
    print("- detik")
    print("- menit")
    print("- jam")
    print("- hari")
    print()


def temperature_menu() -> None:
    """Daftar satuan suhu."""
    print()
    print("Satuan Suhu")
    print("- C")
    print("- F")
    print("- K")
    print()


def storage_menu() -> None:
    """Daftar satuan penyimpanan."""
    print()
    print("Satuan Penyimpanan")
    print("- B")
    print("- KB")
    print("- MB")
    print("- GB")
    print("- TB")
    print()


def show_result(value: float, from_unit: str, to_unit: str, result: float) -> None:
    """Menampilkan hasil konversi."""
    line()
    print(f"Nilai Awal : {value} {from_unit}")
    print(f"Hasil      : {result} {to_unit}")
    line()


def show_error(message: str) -> None:
    """Menampilkan pesan error."""
    line()
    print("ERROR")
    print(message)
    line()


def goodbye() -> None:
    """Pesan saat keluar dari aplikasi."""
    line()
    print("Terima kasih telah menggunakan Unit Converter CLI.")
    line()
