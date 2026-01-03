from utils import nilai_kelulusan, parse_list

data_input = input("masukan daftar nilai mahasiswa: ")
data = parse_list(data_input)

batas_lulus = float(input("standar nilai kelulusan : "))

nilai_rata_rata = nilai_kelulusan(data)
print("nilai rata rata mahasiswa:", nilai_rata_rata)

if nilai_rata_rata >= batas_lulus:
    print("keterangan: LULUS")
else:
    print("keterangan: TIDAK LULUS")

