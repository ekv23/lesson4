# Задайте два целых числа. 
# Напишите программу, которая найдёт НОК 
# (наименьшее общее кратное) этих двух чисел.

from random import randint
num_a = randint(3,30)
num_b = randint(3,30) 

max = max(num_a,num_b)
while True:
    if max%num_a == 0 and max%num_b == 0:
        print(f'НОК для чисел {num_a} и {num_b}: {max}')
        break
    else:
        max += 1