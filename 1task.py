# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:    
# 45 -> 101101        
# 3 -> 11         
# 2 -> 10


print('Введите число для преобразования: ')

decimal_num = int(input())
binary_num = ''
while decimal_num > 0:
    binary_num = str(decimal_num % 2) + binary_num
    decimal_num = decimal_num // 2
print(f' В двоичной системе это будет: {binary_num}')