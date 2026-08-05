"""
validator.py

Berisi fungsi-fungsi validasi input pengguna.
"""


def baca_angka(pesan: str) -> float:
    """
    Membaca input angka dari pengguna.

    Parameter:
        pesan (str): Pesan yang ditampilkan.

    Return:
        float
    """

    while True:
        try:
            nilai = float(input(pesan))
            return nilai

        except ValueError:
            print("\nInput harus berupa angka!\n")


def baca_menu() -> str:
    """
    Membaca pilihan menu.

    Return:
        str
    """

    while True:
        pilihan = input("Pilih menu : ").strip()

        if pilihan in ["0", "1", "2", "3", "4", "5", "6"]:
            return pilihan

        print("\nMenu tidak tersedia.\n")
