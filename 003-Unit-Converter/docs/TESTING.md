TESTING - UNIT CONVERTER CLI

Test Strategy

Task 003 menggunakan:

1. Syntax check
2. Unit test
3. CLI manual test
4. Input validation
5. Error handling


UNIT TEST

Jalankan dari directory 003-Unit-Converter:

python -m unittest discover -v

Expected:

Ran 36 tests
OK


SYNTAX CHECK

Jalankan:

python -m py_compile src/*.py tests/*.py

Tidak ada output berarti syntax valid.


CLI TEST

Jalankan:

python -m src.main

Contoh:

Pilih menu: 1
Masukkan nilai: 1000
Dari unit: m
Ke unit: km

Expected:

Hasil : 1.0 km


TEST COVERAGE

Unit test mencakup:

- Panjang
- Berat
- Waktu
- Suhu
- Penyimpanan
- Nilai desimal
- Nilai negatif
- Konversi suhu
- Invalid temperature unit

Total: 36 tests


REGRESSION TEST

Setiap perubahan pada converter:

python -m unittest discover -v

python -m py_compile src/*.py tests/*.py
