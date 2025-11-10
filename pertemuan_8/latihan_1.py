class mahasiswa:
    def __init__(self, nama, nim, jurusan, universitas):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.universitas = universitas

    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Jurusan: {self.jurusan}")
        print(f'Universitas: {self.universitas} \n')

    def ubah_jurusan(self, jurusan_baru):
        self.jurusan = jurusan_baru
        print(f"Jurusan {self.nama} telah diubah menjadi {self.jurusan}")

mahasiswa_1 = mahasiswa("Andi", "123456", "Informatika", "Universitas Pradita")
mahasiswa_2 = mahasiswa("Budi", "654321", "Sistem Informasi", "Universitas Pradita")

mahasiswa_1.tampilkan_info()
mahasiswa_2.tampilkan_info()

def manually_change_major():
    for i in [mahasiswa_1, mahasiswa_2]:
        print(f'apakah ingin mengubah jurusan {i.nama} (yes/no) : ')
        jawaban = input().lower()
        if 'y' in jawaban:
            print("Masukkan jurusan baru:")
            jurusan_baru = input()
            i.ubah_jurusan(jurusan_baru)
        elif 'n' in jawaban:
            print("Jurusan tidak diubah.")
        else:
            print("Input tidak valid.")

def auto_change_major():
    mahasiswa_1.ubah_jurusan("Teknik Komputer")
    mahasiswa_2.ubah_jurusan("Teknik Elektro")

# manually_change_major()
auto_change_major()

print("\nInformasi Mahasiswa yang Diperbarui: \n")
mahasiswa_1.tampilkan_info()
mahasiswa_2.tampilkan_info()


