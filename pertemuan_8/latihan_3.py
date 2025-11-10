class Kendaraan:
    def __init__(self, merk):
        self.merk = merk

    def bergerak(self):
        print(f'Kendaraan {self.merk} sedang bergerak.')


class Mobil(Kendaraan):
    def __init__(self, merk):
        super().__init__(merk)

    def bergerak(self):
        print(f"Mobil {self.merk} sedang melaju di jalan.")

class Motor(Kendaraan):
    def __init__(self, merk, kecepatan = 50):
        super().__init__(merk)
        self.kecepatan = kecepatan

    def bergerak(self):
        print(f"Motor {self.merk} sedang melaju di aspal dengan kecepatan {self.kecepatan}.")

class Pesawat(Kendaraan):
    def __init__(self, merk):
        super().__init__(merk)

    def bergerak(self):
        print(f"Pesawat {self.merk} sedang terbang di udara.")


# k1 = Mobil("Toyota")
# k2 = SepedaMotor("Yamaha")
# k3 = PesawatTerbang("Boeing")
#
# k1.bergerak()
# k2.bergerak()
# k3.bergerak()

def uji_bergerak(kendaraan):
    kendaraan.bergerak()

daftar = [
    Mobil("Toyota"),
    Motor("Honda", 80),
    Pesawat("Boeing"),
]

for i in daftar:
    uji_bergerak(i)
