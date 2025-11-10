import geometry

def latihan_1():
    scores = []

    for index in range(5):
        score = int(input(f'{index + 1}. Masukkan Nilai Siswa: '))
        scores.append(score)

    classification = input('Apakah ingin menampilkan klasifikasi? [yes / no] ')
    if classification.lower() in ['yes', 'y', 'ya']:
        for index in range(len(scores)):
            if scores[index] >= 80:
                print(f'Nilai Siswa adalah {scores[index]} mendapat klasifikasi A')
            elif scores[index] >= 70:
                print(f'Nilai Siswa adalah {scores[index]} mendapat klasifikasi B')
            elif scores[index] >= 60:
                print(f'Nilai Siswa adalah {scores[index]} mendapat klasifikasi C')
            elif scores[index] >= 50:
                print(f'Nilai Siswa adalah {scores[index]} mendapat klasifikasi D')
            else:
                print(f'Nilai Siswa adalah {scores[index]} mendapat klasifikasi E')
    else:
        for index in range(len(scores)):
            print(f'Nilai Siswa adalah {scores[index]}')



def kkm(score, min_score = 60):
    print(f'Nilai minimum untuk mapel ini adalah {min_score}')

    if score >= min_score:
        print(f'Nilai anda adalah {score} maka anda lulus \n')
    else:
        print(f'Nilai anda adalah {score} maka anda tidak lulus \n')

def latihan_2():
    math = float(input('Masukkan Nilai Matematika Siswa: '))
    physics = float(input('Masukkan Nilai Fisika Siswa: '))
    chemistry = float(input('Masukkan Nilai Kimia Siswa: '))

    kkm(math, 80)
    kkm(physics, 70)
    kkm(chemistry)



def latihan_3(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return latihan_3(n - 1) + latihan_3(n - 2)



def latihan_4():
    panjang = int(input('Masukkan panjang persegi panjang: '))
    lebar = int(input('Masukkan lebar persegi panjang: '))
    luas_persegi_panjang, keliling_persegi_panjang = geometry.persegi_panjang(panjang, lebar)
    print(f'Persegi panjang dengan panjang {panjang} lebar {lebar} memiliki Luas {luas_persegi_panjang} dan keliling {keliling_persegi_panjang}')

    print('-------------------------------------')

    sisi = int(input('Masukkan sisi persegi: '))
    luas_persegi, keliling_persegi = geometry.persegi(sisi)
    print(f'Persegi dengan sisi {sisi} memiliki luas {luas_persegi} dan keliling {keliling_persegi}')



# latihan_1()
latihan_2()
# print(latihan_3(int(input('Masukkan angka fibonacci ke-n: '))))
# latihan_4()