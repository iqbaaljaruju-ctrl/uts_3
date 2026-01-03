from utils import potong_desimal

bilangan = float(input("Masukkan bilangan desimal: "))

digit_hilangkan = int(input("2. Masukkan jumlah digit : "))

print(f"Hasil: {potong_desimal(bilangan, digit_hilangkan)}")
