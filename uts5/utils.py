import math

def hitung_kubus(sisi):
    volume = sisi ** 3
    luas_permukaan = 6 * (sisi ** 2)
    return volume, luas_permukaan

def hitung_balok(panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi
    luas_permukaan = 2 * ((panjang*lebar) + (panjang*tinggi) + (lebar*tinggi))
    return volume, luas_permukaan

def hitung_kerucut(jari_jari, tinggi):
    sisi_miring = math.sqrt(jari_jari**2 + tinggi**2)
    volume = (1/3) * math.pi * jari_jari**2 * tinggi
    luas_permukaan = math.pi * jari_jari * (jari_jari + sisi_miring)
    return volume, luas_permukaan

def hitung_tabung(jari_jari, tinggi):
    volume = math.pi * jari_jari**2 * tinggi
    luas_permukaan = 2 * math.pi * jari_jari * (jari_jari + tinggi)
    return volume, luas_permukaan

def hitung_bola(jari_jari):
    volume = (4/3) * math.pi * jari_jari**3
    luas_permukaan = 4 * math.pi * jari_jari**2
    return volume, luas_permukaan

def hitung_limas_segiempat(alas_sisi, tinggi_limas):
    luas_alas = alas_sisi ** 2
    volume = (1/3) * luas_alas * tinggi_limas
    luas_sisi_tegak = 4 * (0.5 * alas_sisi * math.sqrt((alas_sisi/2)**2 + tinggi_limas**2))
    luas_permukaan = luas_alas + luas_sisi_tegak
    return volume, luas_permukaan

def hitung_limas_segitiga(alas_alas, alas_tinggi, tinggi_limas):
    luas_alas = 0.5 * alas_alas * alas_tinggi
    volume = (1/3) * luas_alas * tinggi_limas
    sisi_miring = math.sqrt((alas_alas/2)**2 + tinggi_limas**2)
    luas_sisi_tegak = 3 * (0.5 * alas_alas * sisi_miring)
    luas_permukaan = luas_alas + luas_sisi_tegak
    return volume, luas_permukaan

def hitung_limas_belahketupat(diagonal1, diagonal2, tinggi_limas):
    luas_alas = 0.5 * diagonal1 * diagonal2
    volume = (1/3) * luas_alas * tinggi_limas
    sisi_alas = 0.5 * math.sqrt(diagonal1**2 + diagonal2**2)
    luas_sisi_tegak = 4 * (0.5 * sisi_alas * math.sqrt((sisi_alas/2)**2 + tinggi_limas**2))
    luas_permukaan = luas_alas + luas_sisi_tegak
    return volume, luas_permukaan

def hitung_limas_trapesium(sisi_sejajar1, sisi_sejajar2, tinggi_trapesium, tinggi_limas):
    luas_alas = 0.5 * (sisi_sejajar1 + sisi_sejajar2) * tinggi_trapesium
    volume = (1/3) * luas_alas * tinggi_limas
    sisi_miring_trapesium = math.sqrt(((sisi_sejajar1 - sisi_sejajar2)/2)**2 + tinggi_trapesium**2)
    luas_sisi_tegak = (sisi_sejajar1 + sisi_sejajar2 + 2*sisi_miring_trapesium) * tinggi_limas * 0.5
    luas_permukaan = luas_alas + luas_sisi_tegak
    return volume, luas_permukaan
