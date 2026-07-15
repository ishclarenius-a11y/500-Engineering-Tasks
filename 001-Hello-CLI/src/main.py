def line():
    print("=" * 50)


def header():
    line()
    print("            HELLO CLI")
    print("        500 ENGINEERING TASKS")
    line()


def get_profile():
    print("\nSilakan isi data berikut:\n")

    profile = {
        "Nama": input("Nama      : "),
        "Umur": input("Umur      : "),
        "Kota": input("Kota      : "),
        "Cita-cita": input("Cita-cita : ")
    }

    return profile


def show_profile(profile):
    print()
    line()
    print("PROFIL PENGGUNA")
    line()

    for key, value in profile.items():
        print(f"{key:<10}: {value}")

    line()
    print("Selamat belajar Software Engineering!")
    line()


def main():
    header()
    profile = get_profile()
    show_profile(profile)


if __name__ == "__main__":
    main()
