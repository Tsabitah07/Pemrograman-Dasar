f = open('data.txt', mode='r', encoding='utf-8')
# mode:
# 'r'  -> read (baca) (default)
# 'w'  -> write (tulis, overwrite)
# 'a'  -> append (tambah di akhir)
# 'x'  -> create (gagal kalau sudah ada)
# 'b'  -> binary (gabungkan: 'rb', 'wb')
# 't'  -> text (default)
# '+'  -> read/write (contoh: 'r+')

# baca seluruh isi
with open('data.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# baca per baris -> list
with open('data.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# iterasi baris (hemat memori)
with open('data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.rstrip('\n'))

# overwrite (membuat/menimpa)
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write('Halo dunia\n')
    f.writelines(['baris1\n', 'baris2\n'])

# append (menambah di akhir)
with open('output.txt', 'a', encoding='utf-8') as f:
    f.write('Tambahan baris\n')
