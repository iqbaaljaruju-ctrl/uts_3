from utils import parse_harga, total_harga, hitung_pajak, format_rp

print("1. Masukkan daftar harga barang :")
harga = parse_harga(input())

total = total_harga(harga)
pajak = hitung_pajak(total)
total_akhir = total + pajak

print(f"Total pembayaran: {format_rp(total)}")
print(f"Pajak: {format_rp(pajak)}")
print(f"Total pembayaran: {format_rp(total_akhir)}")
