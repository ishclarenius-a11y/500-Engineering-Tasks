#!/usr/bin/env python3
"""
main.py

Entry point aplikasi Scientific Calculator.
"""

from calculator import (
    tambah,
    kurang,
    kali,
    bagi,
    pangkat,
    modulus,
)

from menu import (
    header,
    menu,
    hasil,
    error,
    keluar,
)

from validator import (
    baca_angka,
    baca_menu,
)


def proses_perhitungan(pilihan: str, angka1: float, angka2: float) -> float:
    """
    Menentukan operasi berdasarkan menu.
    """

    if pilihan == "1":
        return tambah(angka1, angka2)

    elif pilihan == "2":
        return kurang(angka1, angka2)

    elif pilihan == "3":
        return kali(angka1, angka2)

    elif pilihan == "4":
        return bagi(angka1, angka2)

    elif pilihan == "5":
        return pangkat(angka1, angka2)

    elif pilihan == "6":
        return modulus(angka1, angka2)

    raise ValueError("Menu tidak dikenali.")


def main():
    """
    Program utama.
    """

    header()

    while True:

        menu()

        pilihan = baca_menu()

        if pilihan == "0":
            keluar()
            break

        angka1 = baca_angka("Masukkan angka pertama : ")
        angka2 = baca_angka("Masukkan angka kedua   : ")

        try:

            nilai = proses_perhitungan(
                pilihan,
                angka1,
                angka2,
            )

            hasil(nilai)

        except ZeroDivisionError as e:
            error(str(e))

        except Exception as e:
            error(str(e))


if __name__ == "__main__":
    main()
