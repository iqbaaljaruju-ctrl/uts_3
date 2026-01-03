from utils import *
import os

def tampil_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("1. Persegi\n2. Persegi Panjang\n3. Segitiga\n4. Jajar Genjang\n5. Layang-Layang")
    print("6. Belah Ketupat\n7. Trapesium\n8. Lingkaran\n9. Heksagon\n10. Pentagon\n11. Keluar")

while True:
    tampil_menu()
    try: pilihan = int(input("\nPilih bangun datar: "))
    except:
        print("Input salah!")
        input(" ")
        continue

    if pilihan == 1:
        s = float(input("Sisi: "))
        k, l = hitung_persegi(s)
    elif pilihan == 2:
        p, lbr = float(input("Panjang: ")), float(input("Lebar: "))
        k, l = hitung_persegi_panjang(p, lbr)
    elif pilihan == 3:
        a, t, s1, s2, s3 = float(input("Alas: ")), float(input("Tinggi: ")), float(input("Sisi1: ")), float(input("Sisi2: ")), float(input("Sisi3: "))
        k, l = hitung_segitiga(a, t, s1, s2, s3)
    elif pilihan == 4:
        a, t, sm = float(input("Alas: ")), float(input("Tinggi: ")), float(input("Sisi miring: "))
        k, l = hitung_jajar_genjang(a, t, sm)
    elif pilihan == 5:
        d1, d2, s1, s2 = float(input("Diagonal1: ")), float(input("Diagonal2: ")), float(input("Sisi1: ")), float(input("Sisi2: "))
        k, l = hitung_layang_layang(d1, d2, s1, s2)
    elif pilihan == 6:
        d1, d2, s = float(input("Diagonal1: ")), float(input("Diagonal2: ")), float(input("Sisi: "))
        k, l = hitung_belah_ketupat(d1, d2, s)
    elif pilihan == 7:
        s1, s2, s3, s4, t = float(input("Sisi sejajar1: ")), float(input("Sisi sejajar2: ")), float(input("Sisi tidak sejajar1: ")), float(input("Sisi tidak sejajar2: ")), float(input("Tinggi: "))
        k, l = hitung_trapesium(s1, s2, s3, s4, t)
    elif pilihan == 8:
        r = float(input("Jari-jari: "))
        k, l = hitung_lingkaran(r)
    elif pilihan == 9:
        s = float(input("Sisi: "))
        k, l = hitung_heksagon(s)
    elif pilihan == 10:
        s = float(input("Sisi: "))
        k, l = hitung_pentagon(s)
    elif pilihan == 11:
        print("Program selesai!")
        break
    else:
        print("Pilihan tidak valid!")
        input(" ")
        continue

    print(f"Keliling: {k:.1f}\nLuas: {l:.1f}")
    input(" ")
