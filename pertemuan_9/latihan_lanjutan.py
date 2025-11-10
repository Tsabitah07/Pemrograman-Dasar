import math
from datetime import datetime

# Custom exceptions
class NamaKosongError(Exception):
    pass

class UsiaTidakValidError(Exception):
    pass

class EmailTidakValidError(Exception):
    pass

class SaldoTidakCukupError(Exception):
    pass

# 1. Form validation
def validate_form(name: str, age_str: str, email: str):
    name = name.strip()
    if not name:
        raise NamaKosongError("Nama tidak boleh kosong.")

    try:
        age = int(age_str)
    except ValueError:
        raise UsiaTidakValidError("Usia harus berupa angka.")
    if not (0 <= age <= 120):
        raise UsiaTidakValidError("Usia harus antara 0 dan 120.")

    if "@" not in email:
        raise EmailTidakValidError("Email harus mengandung karakter '@'.")
    return {"name": name, "age": age, "email": email}

def form_demo():
    print("== Form Validation Demo ==")
    name = input("Nama: ")
    age = input("Usia: ")
    email = input("Email: ")
    try:
        data = validate_form(name, age, email)
    except (NamaKosongError, UsiaTidakValidError, EmailTidakValidError) as e:
        print("Validasi gagal:", e)
    else:
        print("Validasi berhasil:", data)
    print()

# 2. ATM simulation
class ATM:
    def __init__(self, initial_balance: float):
        self.balance = float(initial_balance)

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise SaldoTidakCukupError("Saldo tidak cukup untuk penarikan ini.")
        self.balance -= amount
        return self.balance

def atm_demo():
    print("== ATM Demo ==")

    while True:
        balance_in = input("Masukkan saldo awal (atau 'quit' untuk keluar): ")
        if balance_in.lower() == 'quit':
            print("Keluar dari ATM demo.")
            return
        try:
            atm = ATM(float(balance_in))
            break
        except ValueError:
            print("Masukkan angka valid untuk saldo.")

    while True:
        amt = input("Masukkan jumlah penarikan (atau 'quit' untuk selesai): ")
        if amt.lower() == 'quit':
            print("\nSelesai ATM demo.")
            break
        try:
            amount = float(amt)
        except ValueError:
            print("\nJumlah harus berupa angka.")
            continue
        try:
            new_bal = atm.withdraw(amount)
            print(f"\nPenarikan berhasil. Sisa saldo: {new_bal:.2f}")
        except SaldoTidakCukupError as e:
            print("\nKesalahan:", e)
        finally:
            print(f"\nSaldo akhir (ditampilkan selalu): {atm.balance:.2f}")
    print()

# 3. Error capture and logging
def run_operations_and_log():
    print("== Operations and Logging Demo ==")
    ops = [
        ("division_by_zero", lambda: 10 / 0),
        ("sqrt_negative", lambda: math.sqrt(-1)),
        ("bad_conversion", lambda: int("abc")),
        ("valid_op", lambda: math.sqrt(16)),
    ]
    log_path = "error.log"
    for name, func in ops:
        try:
            result = func()
            print(f"{name}: result = {result}")
        except Exception as e:
            timestamp = datetime.now().isoformat(sep=' ', timespec='seconds')
            log_line = f"{timestamp} | {name} | {e.__class__.__name__} | {e}\n"
            with open(log_path, "a", encoding="utf-8") as f:
                f.write(log_line)
            print(f"{name}: error logged ({e.__class__.__name__}).")
    print(f"Errors (if any) appended to {log_path}\n")

if __name__ == "__main__":
    # form_demo()
    atm_demo()
    # run_operations_and_log()