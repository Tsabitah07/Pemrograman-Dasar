#1
def latihan_1():
    angka_1 = float(input("Masukkan angka : "))
    angka_2 = int(angka_1)

    hasil_angka = angka_1 - angka_2
    print(f"Fraksi angka : {hasil_angka:.3f}")



#2
def latihan_2():
    angka_awal = float(input("Masukkan angka : "))

    angka_int = int(angka_awal)
    hasil_1 = float(angka_int / 1000)
    print(hasil_1)

    hasil_2 = float(angka_awal - angka_int) * 1000
    print(hasil_2)

    hasil_akhir = hasil_1 + hasil_2

    print(f"hasil angka : {hasil_akhir:.3f}")



#3
def latihan_3_1():
    a = input("Masukkan angka pertama = ")
    b = input("Masukkan angka kedua = ")

    print(f"Angka Awal A: {a} B: {b}")

    a, b = b, a

    print(f"Angka Akhir A: {a} B: {b}")



def latihan_3_2():
    a = input("Masukkan angka pertama = ")
    b = input("Masukkan angka kedua = ")

    print(f"Angka Awal A: {a} B: {b}")

    c = a
    a = b
    b = c

    print(f"Angka Akhir A: {a} B: {b}")



def latihan_3_3():
    a = int(input("Masukkan angka pertama = "))
    b = int(input("Masukkan angka kedua = "))

    print(f"Angka Awal A: {a} B: {b}")

    a += b
    b = a - b
    a -= b

    print(f"Angka Akhir A: {a} B: {b}")



# latihan_1()
# latihan_2()
# latihan_3_1()
# latihan_3_2()
latihan_3_3()