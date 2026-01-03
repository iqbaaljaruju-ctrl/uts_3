from utils import *
import os

def tampil_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("1. Kubus\n2. Balok\n3. Kerucut\n4. Tabung\n5. Bola")
    print("6. Limas Segiempat\n7. Limas Segitiga\n8. Limas Belahketupat\n9. Limas Trapesium\n10. Keluar")

while True:
    tampil_menu()
    try: pilihan = int(input("\nPilih bangun ruang: "))
    except:
        print("Input salah!")
        input()  
        continue

    if pilihan == 1:
        s = float(input("Sisi: "))
        v, lp = hitung_kubus(s)
    elif pilihan == 2:
        p, l, t = float(input("Panjang: ")), float(input("Lebar: ")), float(input("Tinggi: "))
        v, lp = hitung_balok(p, l, t)
    elif pilihan == 3:
        r, t = float(input("Jari-jari: ")), float(input("Tinggi: "))
        v, lp = hitung_kerucut(r, t)
    elif pilihan == 4:
        r, t = float(input("Jari-jari: ")), float(input("Tinggi: "))
        v, lp = hitung_tabung(r, t)
    elif pilihan == 5:
        r = float(input("Jari-jari: "))
        v, lp = hitung_bola(r)
    elif pilihan == 6:
        s, t = float(input("Sisi alas: ")), float(input("Tinggi limas: "))
        v, lp = hitung_limas_segiempat(s, t)
    elif pilihan == 7:
        aa, at, tl = float(input("Alas segitiga: ")), float(input("Tinggi alas: ")), float(input("Tinggi limas: "))
        v, lp = hitung_limas_segitiga(aa, at, tl)
    elif pilihan == 8:
        d1, d2, tl = float(input("Diagonal1 alas: ")), float(input("Diagonal2 alas: ")), float(input("Tinggi limas: "))
        v, lp = hitung_limas_belahketupat(d1, d2, tl)
    elif pilihan == 9:
        ss1, ss2, tt, tl = float(input("Sisi sejajar1 alas: ")), float(input("Sisi sejajar2 alas: ")), float(input("Tinggi trapesium: ")), float(input("Tinggi limas: "))
        v, lp = hitung_limas_trapesium(ss1, ss2, tt, tl)
    elif pilihan == 10:
        print("Program selesai!")
        break
    else:
        print("Pilihan tidak valid!")
        input()  
        continue

    print(f"Volume: {v:.1f}\nLuas permukaan: {lp:.1f}")
    input()  
