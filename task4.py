# Напишите функцию, которая находит
# наибольший общий делитель двух натуральных чисел
# На входе два числа, на выходе их НОД.

def f(a, b):
    while a != b:
        if  a > b:
            a = a-b
        else:
            b = b - a
    return b
a = int(input())
b = int (input())
print (f(a,b))