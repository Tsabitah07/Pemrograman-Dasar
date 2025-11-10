#1
def latihan_1():
    nilai_1 = float(input("Masukkan nilai pertama = "))
    nilai_2 = float(input("Masukkan nilai kedua = "))
    nilai_3 = float(input("Masukkan nilai ketiga = "))
    nilai_4 = float(input("Masukkan nilai keempat = "))
    nilai_5 = float(input("Masukkan nilai kelima = "))

    average = (nilai_1 + nilai_2 + nilai_3 + nilai_4 + nilai_5) / 5

    print(f"Rata-rata nilai = {average:.2f}")

    if average >= 90:
        print("Predikat = A")
    elif average >= 85:
        print("Predikat = A-")
    elif average >= 80:
        print("Predikat = B+")
    elif average >= 75:
        print("Predikat = B")
    elif average >= 70:
        print("Predikat = B-")
    elif average >= 65:
        print("Predikat = C+")
    elif average >= 60:
        print("Predikat = C")
    elif average >= 55:
        print("Predikat = D")
    else:
        print("Predikat = E")



def latihan_2():
    berat_badan = float(input("Masukkan berat badan (kg) = "))
    tinggi_badan = float(input("Masukkan tinggi badan (cm) = "))

    bmi = berat_badan / ((tinggi_badan / 100) ** 2)

    if bmi < 18.5:
        print(f'bmi = {bmi:.2f}')
        print(f'kategori = Kurus')
    elif bmi < 25:
        print(f'bmi = {bmi:.2f}')
        print(f'kategori = Normal')
    elif bmi < 30:
        print(f'bmi = {bmi:.2f}')
        print(f'kategori = Overweight')
    else:
        print(f'bmi = {bmi:.2f}')
        print(f'kategori = Obesitas')



def latihan_3():
    weight = float(input("Masukkan berat badan (kg) = "))
    height = float(input("Masukkan tinggi badan (cm) = "))

    bmi = weight / ((height / 100) ** 2)
    category = ''

    if bmi < 18.5:
        category = 'Kurus'
    elif bmi < 25:
        category = 'Normal'
    elif bmi < 30:
        category = 'Overweight'
    else:
        category = 'Obesitas'

    match category:
        case 'Kurus':
            print(f'bmi = {bmi:.2f}')
            print(f'kategori = {category}')
            print(f'Saran = Makan lebih banyak makanan bergizi')
        case 'Normal':
            print(f'bmi = {bmi:.2f}')
            print(f'kategori = {category}')
            print(f'Saran = Pertahankan pola makan dan olahraga teratur')
        case 'Overweight':
            print(f'bmi = {bmi:.2f}')
            print(f'kategori = {category}')
            print(f'Saran = Kurangi asupan kalori dan tingkatkan aktivitas fisik')
        case 'Obesitas':
            print(f'bmi = {bmi:.2f}')
            print(f'kategori = {category}')
            print(f'Saran = Konsultasi dengan profesional kesehatan untuk rencana penurunan berat badan')



def latihan_4():
    email = input("Masukkan email = ")
    password = input("Masukkan password = ")

    if "pradita.ac.id" in email and len(password) >= 8:
        print("Login berhasil")
    else:
        print("Login gagal")



def latihan_5():
    operation = input("Masukkan operasi (+, -, *, /) = ")
    num_1 = float(input("Masukkan angka pertama = "))
    num_2 = float(input("Masukkan angka kedua = "))

    match operation:
        case '+':
            result = num_1 + num_2
            print(f"Hasil {num_1} + {num_2} = {result}")
        case '-':
            result = num_1 - num_2
            print(f"Hasil {num_1} - {num_2} = {result}")
        case '*':
            result = num_1 * num_2
            print(f"Hasil {num_1} x {num_2} = {result}")
        case '/':
            if num_2 != 0:
                result = num_1 / num_2
                print(f"Hasil {num_1} : {num_2} = {result}")
            else:
                print("Error: Pembagian dengan nol tidak diperbolehkan.")
        case _:
            print("Operasi tidak dikenali.")



def latihan_6():
    angka = int(input("Masukkan sebuah bilangan bulat: "))

    jenis = "Genap" if angka % 2 == 0 else "Ganjil"
    print(f"{angka} adalah bilangan {jenis}")



# latihan_1()
# latihan_2()
# latihan_3()
# latihan_4()
# latihan_5()
latihan_6()