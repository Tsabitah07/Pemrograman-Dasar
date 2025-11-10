global current_balance

class NotEnoughBalance(Exception):
    def __init__(self, message, balance):
        super().__init__(message)
        self.balance = balance
        self.message = message

    def __str__(self):
        return self.message

class SaldoInputNegative(Exception):
    def __init__(self, message, balance):
        super().__init__(message)
        self.balance = balance
        self.message = message

    def __str__(self):
        return self.message

while True:
    try:
        current_balance = float(input('Input jumlah saldo awal yang ingin anda masukkan : '))

        while True:
            try:
                withdrawal_input = input('\nInput jumlah saldo yang ingin anda tarik : ')
                withdrawal = float(withdrawal_input)
                if withdrawal > current_balance:
                    raise NotEnoughBalance('Saldo yang anda tarik melebihi jumlah saldo awal', current_balance)
                if withdrawal < 0:
                    raise SaldoInputNegative('Anda tidak dapat memasukkan angka negatif', current_balance)

                if current_balance >= withdrawal:
                    current_balance -= withdrawal
            except ValueError:
                print('Input tidak valid. Masukkan angka.')
            except NotEnoughBalance as a:
                print(a.message)
            except SaldoInputNegative as n:
                print(n.message)
            else:
                print(f'Penarikan saldo sebesar {withdrawal} berhasil dilakukan')
            finally:
                print(f'Sisa saldo anda adalah {current_balance}')

            repeat_process = input('\nApakah anda ingin melakukan proses penarikan saldo kembali? (y/n) : ')
            if 'n' in repeat_process.lower() & 'y' not in repeat_process.lower():
                print('\nTerima kasih telah menggunakan layanan ATM kami.')
                break

        break
    except ValueError:
        print('Input tidak valid. Masukkan angka.')
        continue