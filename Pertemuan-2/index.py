from typing import Final



# Mendefinisikan variabel dengan tipe data yang berbeda
nama = "Inas Tsabitah" #string
usia = 18 #int
berat_badan = 50.5 #float
status_mahasiswa = True #bool

print("Nama:", nama)
print("Usia:", usia , "tahun")
print("Berat Badan:", berat_badan, "kg")
print("Status Mahasiswa:", status_mahasiswa)



# Mendefinisikan konstanta
PI : Final = 3.14
Gravitasi : Final = 9.8

print("Nilai PI:", PI)
print("Nilai Gravitasi:", Gravitasi, "m/s^2")

# mencoba mengubah nilai konstanta
PI = 3.14159 # Ini akan menimbulkan peringatan dari alat pemeriksa tipe
print("Nilai PI yang diubah:", PI)



#Konversi Tipe Data
mahasiswa = bool(0)
list_mahasiswa = ["Inas", "Tsabitah"]
list_siswa = ("Tsabitah", "Inas")

if mahasiswa == True:
    print(type(mahasiswa), "Halo Mahasiswa!")
    print(type(list_mahasiswa), list_mahasiswa)
else:
    print(type(mahasiswa), "Halo Siswa!")
    print(type(list_siswa), list_siswa)


angka_str = "45.67"
print("Sebelum konversi:", angka_str , type( angka_str ))

angka_float = float( angka_str )
print("Setelah konversi ke float:", angka_float , type( angka_float ))


angka_str = "45.67"

# angka_int = int( angka_str )
# print(type(angka_int), angka_int)

angka_float = float( angka_str )
angka_int_2 = int( angka_float )
print(type(angka_float), angka_float)
print(type(angka_int_2), angka_int_2)