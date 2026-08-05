"""
menu.py

Mengatur tampilan aplikasi CLI.
"""

APP_NAME = "Scientific Calculator"
VERSION = "1.0.0"


def garis():
    """Menampilkan garis pemisah."""
    print("=" * 45)


def header():
    """Menampilkan judul aplikasi."""
    garis()
    print(APP_NAME)
    print(f"Version : {VERSION}")
    garis()


def menu():
    """Menampilkan daftar menu."""
    print()
    print("Pilih Operasi")
    print("-" * 20)
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Pangkat (**)")
    print("6. Modulus (%)")
    print("0. Keluar")
    print()


def hasil(nilai):
    """Menampilkan hasil perhitungan."""
    garis()
    print(f"Hasil : {nilai}")
    garis()


def error(pesan):
    """Menampilkan pesan error."""
    garis()
    print("ERROR")
    print(pesan)
    garis()


def keluar():
    """Pesan ketika program selesai."""
    garis()
    print("Terima kasih telah menggunakan program ini.")
    garis()
