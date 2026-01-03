def total_harga(data):
    return sum(data)

def parse_list(list_string):
    return list(map(int, list_string.split()))

def hitung_diskon(total):
    if total > 50000:
        return total * 0.01  # diskon 0,1%
    return 0