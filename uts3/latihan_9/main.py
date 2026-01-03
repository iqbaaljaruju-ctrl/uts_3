from utils import hitung_total

jumlah = int(input(" Jumlah mahasiswa: "))

daftar_rata_rata = []

for i in range(jumlah):
    nilai = list(map(int, input(f"   Nilai mahasiswa {i+1}: ").split()))
    total_nilai = hitung_total(nilai)
    rata_rata = total_nilai / len(nilai)
    daftar_rata_rata.append(rata_rata)

for i in range(jumlah):
    print(f"Nilai rata-rata mahasiswa {i+1}: {daftar_rata_rata[i]:.2f}")
