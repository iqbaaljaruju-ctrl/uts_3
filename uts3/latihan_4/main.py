# main.py
from utils import total_harga, parse_list, hitung_diskon

# 1. Masukkan daftar harga barang
print("Masukkan daftar harga barang yang dibeli :")
data = input()
harga = parse_list(data)

total_sebelum = total_harga(harga)
diskon = hitung_diskon(total_sebelum)
total_setelah = total_sebelum - diskon

print(f"Total pembayaran: {total_sebelum}")

print(f"Jumlah diskon: {diskon}")

print(f"Total pembayaran : {total_setelah}")
