from utils import parse_nilai_uang, format_rupiah

print("1. Masukkan nilai uang :")
input_nilai = input()

nilai_angka = parse_nilai_uang(input_nilai)
nilai_format_rupiah = format_rupiah(nilai_angka)

print(f"2. Nilai rupiah: {nilai_format_rupiah}")
