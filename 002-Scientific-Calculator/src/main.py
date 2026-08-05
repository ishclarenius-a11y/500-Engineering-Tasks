#!/usr/bin/env python3
"""
Scientific Calculator CLI
Task 002 - 500 Engineering Tasks
Author: Corv

Versi:
- Penjumlahan
- Pengurangan
- Perkalian
- Pembagian
- Pangkat
- Modulus
- Validasi input
"""

APP_NAME = "Scientific Calculator"
VERSION = "1.0.0"


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
    """Mengembalikan hasil pembagian."""
    if b == 0:
        raise ZeroDivisionError("Pembagian dengan nol tidak diperbolehkan.")
    return a / b


def pangkat(a: float, b: float) -> float:
    """Mengembalikan hasil perpangkatan."""
    return a ** b


def modulus(a: float, b: float) -> float:
    """Mengembalikan sisa hasil bagi."""
    if b == 0:
        raise ZeroDivisionError("Modulus dengan nol tidak diperbolehkan.")
    return a % b


def tampilkan_header() -> None:
    print("=" * 40)
    print(APP_NAME)
    print(f"Version : {VERSION}")
    print("=" * 40)


def tampilkan_menu() -> None:
    print("\nPilih operasi:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Pangkat (**)")
    print("6. Modulus (%)")
    print("0. Keluar")


def baca_angka(pesan: str) -> float:
    while True:
        try:
            return float(input(pesan))
        except ValueError:
            print("Input harus berupa angka.")


def hitung(pilihan: str, a: float, b: float) -> float:
    if pilihan == "1":
        return tambah(a, b)

    if pilihan == "2":
        return kurang(a, b)

    if pilihan == "3":
        return kali(a, b)

    if pilihan == "4":
        return bagi(a, b)

    if pilihan == "5":
        return pangkat(a, b)

    if pilihan == "6":
        return modulus(a, b)

    raise ValueError("Menu tidak tersedia.")


def main() -> None:
    tampilkan_header()

    while True:
        tampilkan_menu()

        pilihan = input("\nMasukkan pilihan: ").strip()

        if pilihan == "0":
            print("\nTerima kasih.")
            break

        try:
            angka1 = baca_angka("Angka pertama : ")
            angka2 = baca_angka("Angka kedua   : ")

            hasil = hitung(pilihan, angka1, angka2)

            print("-" * 40)
            print(f"Hasil = {hasil}")
            print("-" * 40)

        except ZeroDivisionError as error:
            print(f"ERROR : {error}")

        except ValueError as error:
            print(f"ERROR : {error}")

        except KeyboardInterrupt:
            print("\nProgram dihentikan pengguna.")
            break


if __name__ == "__main__":
    main()
