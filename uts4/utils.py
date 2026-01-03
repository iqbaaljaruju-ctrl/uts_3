import math

def hitung_persegi(sisi):
    keliling = 4 * sisi
    luas = sisi ** 2
    return keliling, luas

def hitung_persegi_panjang(panjang, lebar):
    keliling = 2 * (panjang + lebar)
    luas = panjang * lebar
    return keliling, luas

def hitung_segitiga(alas, tinggi, sisi1, sisi2, sisi3):
    keliling = sisi1 + sisi2 + sisi3
    luas = 0.5 * alas * tinggi
    return keliling, luas

def hitung_jajar_genjang(alas, tinggi, sisi_miring):
    keliling = 2 * (alas + sisi_miring)
    luas = alas * tinggi
    return keliling, luas

def hitung_layang_layang(diagonal1, diagonal2, sisi1, sisi2):
    keliling = 2 * (sisi1 + sisi2)
    luas = 0.5 * diagonal1 * diagonal2
    return keliling, luas

def hitung_belah_ketupat(diagonal1, diagonal2, sisi):
    keliling = 4 * sisi
    luas = 0.5 * diagonal1 * diagonal2
    return keliling, luas

def hitung_trapesium(sisi1, sisi2, sisi3, sisi4, tinggi):
    keliling = sisi1 + sisi2 + sisi3 + sisi4
    luas = 0.5 * (sisi1 + sisi2) * tinggi
    return keliling, luas

def hitung_lingkaran(jari_jari):
    keliling = 2 * math.pi * jari_jari
    luas = math.pi * (jari_jari ** 2)
    return keliling, luas

def hitung_heksagon(sisi):
    keliling = 6 * sisi
    luas = (3 * math.sqrt(3) / 2) * (sisi ** 2)
    return keliling, luas

def hitung_pentagon(sisi):
    keliling = 5 * sisi
    luas = (5 * sisi ** 2) / (4 * math.tan(math.pi / 5))
    return keliling, luas
