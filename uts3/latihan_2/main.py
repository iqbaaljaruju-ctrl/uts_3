from utils import total_harga, parse_list

data_input = input("masukkan daftar harga barang yang dibeli : ")
data = parse_list(data_input)

total = total_harga(data)
print("Total harga barang:", total)