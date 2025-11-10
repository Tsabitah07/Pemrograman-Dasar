class EmptyName(Exception):
    def __init__(self, name, message):
        self.message = message
        self.name = name
        super().__init__(message)

    def __str__(self):
        return self.message


class InvalidAge(Exception):
    def __init__(self, age, message):
        self.message = message
        self.age = age
        super().__init__(message)

    def __str__(self):
        return self.message


class InvalidEmail(Exception):
    def __init__(self, email, message):
        self.message = message
        self.email = email
        super().__init__(message)

    def __str__(self):
        return self.message


def add_name():
    input_name = input('Masukkan username anda : ')
    if input_name == '':
        raise EmptyName(input_name, 'Nama tidak boleh kosong, silahkan coba kembali')
    else:
        return input_name


def add_age():
    input_age = int(input('Masukkan Usia Anda : '))
    if input_age < 0:
        raise InvalidAge(input_age, "Usia tidak bisa menggunakan sebuah angka negatif")
    elif input_age > 120:
        raise InvalidAge(input_age, 'Usia anda terlalu tua untuk seorang manusia')
    else:
        return input_age


def add_email():
    input_email = input('Masukkan Email anda : ')
    if '@' not in input_email:
        raise InvalidEmail(input_email, 'Email yang anda masukkan tidak valid (tidak ada "@")')
    else:
        return input_email


try:
    name = add_name()
    age = add_age()
    email = add_email()
except EmptyName as n:
    print(n.message)
except InvalidAge as u:
    print(u.message)
except InvalidEmail as e:
    print(e.message)
else:
    print('\nData yang anda masukkan adalah sebagai berikut:')
    print(f'Username : {name}')
    print(f'Usia     : {age}')
    print(f'Email    : {email}')