# Напишите функцию, которая сокращает дробь вида M/N.
# Где M и N - наутральные числа.
# В качестве аргументов она принимает числитель и знаменатель,
# выводит числитель и знаменатель после сокращения
#
# Пример:
# Ввод:
# 25 15
# Вывод:
# 5 3


def h(a,b):

        for j in range (2, a+1):

            if a%j==0:
                if b%j == 0:
                    a = a // j
                    b = b // j
                    for j in range(2, a + 1):

                        if a % j == 0:
                            if b % j == 0:
                                a = a // j
                                b = b // j

        return(a,b)


a = int(input())
b = int(input())
print(h(a,b))
