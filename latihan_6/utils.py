def parse_harga(input_str):
    return list(map(int, input_str.split()))

def total_harga(data):
    return sum(data)

def hitung_pajak(total):
    return total * 0.1  # Pajak 10%

def format_rp(nilai):
    return f"Rp {nilai:,}".replace(",", ".")
