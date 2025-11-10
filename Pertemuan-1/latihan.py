#1
def latihan_1():
    nama = input("Masukkan nama Anda: ")
    prodi = input("Masukkan program studi Anda: ")
    angkatan = input("Masukkan angkatan Anda: ")

    print("Halo, nama saya" , nama , "dari program studi", prodi , "angkatan" , angkatan)
    print(f'Halo, nama saya {nama} dari program studi {prodi} angkatan {angkatan}')



#2
def latihan_2():
    penulis = input("Masukkan nama penulis Quote: ")
    quote = input("Masukkan Quote: ")

    print(f"Menurut {penulis}, \"{quote}\"")



#3
def latihan_3():
    jadwal = []

    banyak_jadwal = int(input("Masukkan banyak jadwal: "))

    for i in range(banyak_jadwal):
        hari = input("Masukkan hari: ")
        waktu = input("Masukkan waktu: ")
        matkul = input("Masukkan mata kuliah: ")

        jadwal.append([hari, waktu, matkul])

    print(f"\tHari  \tWaktu \tMata Kuliah")
    for item in jadwal:
        print(f"\t{item[0]}  \t{item[1]}  \t{item[2]}")



# latihan_1()
# latihan_2()
latihan_3()