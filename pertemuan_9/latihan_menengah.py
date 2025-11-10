# python
class NilaiNegatifError(Exception):
    pass

def cek_positif(n):
    if n < 0:
        raise NilaiNegatifError("Nilai tidak boleh negatif!")

def main():
    try:
        a = float(input("Masukkan pembilang: "))
        b = float(input("Masukkan penyebut: "))
        cek_positif(a)
        cek_positif(b)
        hasil = a / b
    except ValueError:
        print("ValueError: Input bukan angka.")
    except NilaiNegatifError as e:
        print(e)
    except ZeroDivisionError:
        print("ZeroDivisionError: Penyebut tidak boleh nol.")
    else:
        print(f"Hasil :", hasil)
    finally:
        print("Selesai memproses data.")

if __name__ == "__main__":
    main()