def divide_numbers():
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        result = a / b
    except ZeroDivisionError:
        print("Error: Pembagian dengan nol tidak diperbolehkan.")
    except ValueError:
        print("Input tidak valid: masukkan angka.")
    else:
        print(f"Hasil: {result}")

def validate_integer_input():
    try:
        n = int(input("Masukkan sebuah angka bulat: "))
    except ValueError:
        print("Input tidak valid: masukkan angka bulat.")
    else:
        print(f"Angka yang dimasukkan: {n}")

def read_file_safely():
    filename = input("Masukkan nama file untuk dibaca: ")
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print("Error: File tidak ditemukan.")
    finally:
        print("\nOperasi selesai, terima kasih.")

if __name__ == "__main__":
    # divide_numbers()
    # validate_integer_input()
    read_file_safely()