import datetime



def persegi_panjang():
    panjang = int(input("Masukkan panjang [cm] = "))
    lebar = int(input("Masukkan lebar [cm] = "))

    luas = panjang * lebar
    print(f"luas persegi panjang dengan panjang {panjang} cm lebar {lebar} cm adalah {luas}cm2")



def lingkaran():
    pi_7 = 22 / 7
    pi_selain_7 = 3.14

    r = int(input("Masukkan jari - jari [cm] = "))

    if r % 7 == 0:
        luas = pi_7 * r ** 2
        print(f"Luas lingkaran dengan jari - jari {r} adalah {luas} cm2")
    else:
        luas = pi_selain_7 * r ** 2
        print(f"Luas lingkaran dengan jari - jari {r} adalah {luas} cm2")



def usia():
    tahun_lahir = int(input("Masukkan tahun lahir = "))

    usia = datetime.date.today().year - tahun_lahir

    print(f"Lahir tahun {tahun_lahir} berarti sekarang berusia {usia} tahun")



# persegi_panjang()
lingkaran()
# usia()