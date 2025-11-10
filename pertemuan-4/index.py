import aritmatika

# print(aritmatika.add(20, 30))
# print(aritmatika.subtract(20, 30))
# print(aritmatika.multiply(20, 30))
# print(aritmatika.divide(20, 30))
# print(aritmatika.power(20, 30))

def fibonacci(n):
   if n <= 1:
        return 0
   elif n == 2:
        return 1
   else:
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input('masukkan angka fibonacci yang ingin anda ketahui : '))
print(fibonacci(n))