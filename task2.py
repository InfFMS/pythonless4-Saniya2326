# Напишите функцию number_to_words(num), которая принимает
# в качестве аргумента натуральное число num и возвращает
# его словесное описание на русском языке.
#
# Примечание 1.
# Считайте, что число 1 ≤ num ≤ 99.
#
# Примечание 2.
# Следующий программный код:
#
# print(number_to_words(7))
# print(number_to_words(85))
# должен выводить:
from enum import nonmember


# семь
# восемьдесят пять
def f(n):


a = n // 10
b = n % 10

name

    odin =('один')
    dv =('дв')
tri=('три')
cetir=('четыр')
pat=('пят')
sh=('шест')
sem=('сем')
vos=('восем')
deva=('девя')
na=('на')
dzat=('дцать')
sorok=('сорок')
s = ('а')
m=('ь')
nosto=('носто')
tm=('ть')
t = ('т')
e = ('е')

    if a != 0:
        if a ==1:
            if  b == 1:
                name = odin + na + dzat
            if b == 2:
                name = dv + e + na + dzat
            if b == 3:
                name = tri + na + dzat
            if b == 4:
                name = cetir + na + dzat
            if b == 5:
                name = pat + na + dzat
            if b == 6:
                name = sh + na + dzat

            if b == 7:
                name = sem + na + dzat
            if b == 8:
                name = vos + na + dzat
            if b == 9:
                name = deva + t + na + dzat
        if a == 2:

    else:
