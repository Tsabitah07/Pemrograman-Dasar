from decimal import Decimal

#1
def latihan_1():
    angka_1 = float(input("Masukkan angka : "))
    angka_2 = int(angka_1)

    hasil_angka = angka_1 - angka_2

    angka_str = len(str(angka_1)) - len(str(angka_2)) - 1

    print(f"Fraksi angka : {hasil_angka:.{angka_str}f}")



#2
def latihan_2():
    angka_awal = Decimal(input("Masukkan angka : "))
    angka_static_1 = 1
    angka_static_2 = 1

    angka_int = int(angka_awal)
    angka_str_1 = len(str(angka_int))

    for i in range (angka_str_1):
        angka_static_1 *= 10

    hasil_1 = Decimal(angka_int / angka_static_1)
    print(hasil_1)

    angka_str_2 = len(str(angka_awal)) - angka_str_1 - 1
    for j in range (angka_str_2):
        angka_static_2 *= 10

    hasil_2 = int( Decimal(angka_awal - angka_int) * angka_static_2)
    print(hasil_2)

    hasil_akhir = hasil_1 + hasil_2

    print(f"hasil angka : {hasil_akhir:.{angka_str_1}f}")



#3
def latihan_3():
    a = input("Masukkan angka pertama = ")
    b = input("Masukkan angka kedua = ")

    print(f"Angka Awal A: {a} B: {b} \n-----------------")

    a, b = b, a

    print(f"Angka Akhir A: {a} B: {b}")



def gemini():
    angka = float(input("Masukkan sebuah bilangan bulat: "))
    jumlah_digit = len(str(angka))
    print(f"Jumlah digit dari {angka} adalah {jumlah_digit}")
    print(type(jumlah_digit))



# latihan_1()
latihan_2()
# latihan_3()
# gemini()