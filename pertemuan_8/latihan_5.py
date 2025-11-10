import math
import re


class BangunDatar:
    def luas(self):
        print(f'Harus di override di kelas turunan')

    def keliling(self):
        print(f'Harus di override di kelas turunan')

class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi

    def keliling(self):
        return 4 * self.sisi

class PersegiPanjang(BangunDatar):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)

class Lingkaran(BangunDatar):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        return math.pi * self.jari_jari ** 2

    def keliling(self):
        return 2 * math.pi * self.jari_jari

class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def luas(self):
        return self.alas * self.tinggi / 2

class SegitigaSamaSisi(Segitiga):
    def __init__(self, alas, tinggi):
        super().__init__(alas, tinggi)

    def keliling(self):
        sisi_miring = math.sqrt((self.alas / 2) ** 2 + self.tinggi ** 2)
        return 2 * sisi_miring + self.alas

class SegitigaSikuSiku(Segitiga):
    def __init__(self, alas, tinggi):
        super().__init__(alas, tinggi)

    def keliling(self):
        sisi_miring = math.sqrt(self.alas ** 2 + self.tinggi ** 2)
        return self.alas + self.tinggi + sisi_miring


list_bangun_datar = [
    Persegi(4),
    PersegiPanjang(5, 3),
    Lingkaran(7),
    SegitigaSamaSisi(6, 4),
    SegitigaSikuSiku(6, 4),
]

def format_class_name(name: str) -> str:
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', name)

for i in list_bangun_datar:
    print(format_class_name(i.__class__.__name__))
    print(f'Luas: {i.luas():.2f}')
    print(f'Keliling: {i.keliling():.2f}\n')