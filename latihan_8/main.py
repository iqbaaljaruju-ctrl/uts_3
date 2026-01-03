from utils import hitung_total

jumlah = int(input("Jumlah konsumen: "))

daftar_total = []

for i in range(jumlah):
    harga = list(map(int, input(f"  masukan harga barang yang dibeli Konsumen {i+1}: ").split()))
    daftar_total.append(hitung_total(harga))

for i in range(jumlah):
    print(f"Total pembayaran konsumen {i+1}: Rp {daftar_total[i]:,}".replace(",", "."))
