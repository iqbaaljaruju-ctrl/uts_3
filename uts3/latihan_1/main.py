from utils import menghitung_nilai_terbesar, menghitung_nilai_terkecil, parse_list

data = input("masukan data: ")
data = parse_list(data)

nilai_terbesar = menghitung_nilai_terbesar(data)
nilai_terkecil = menghitung_nilai_terkecil(data)

print("nilai terbesar: ", nilai_terbesar)
print("nilai terkecil: ", nilai_terkecil)

