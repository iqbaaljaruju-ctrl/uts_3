def parse_nilai_uang(input_string):
    """Ubah input string angka menjadi nilai numerik"""
    try:
        return int(input_string)
    except ValueError:
        print("Input tidak valid! Harap masukkan angka tanpa karakter lain.")
        return 0

def format_rupiah(nilai):
    """Format nilai numerik menjadi string dengan format Rp X.XXX"""
    return f"Rp {nilai:,}".replace(",", ".")
