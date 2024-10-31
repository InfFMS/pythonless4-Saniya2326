# Напишите функцию is_valid_triangle(side1, side2, side3),
# которая принимает в качестве аргументов три натуральных числа,
# и возвращает значение True, если существует невырожденный треугольник
# со сторонами side1, side2, side3, или False в противном случае.

def is_valid_triangle (s1, s2, s3):
    if s1+s2>s3:
        if s2+s3>s1:
            if s1+s3>s2:
                return True
    return False
s1 = int(input())
s2 = int(input())
s3 =  int(input())
if is_valid_triangle (s1, s2, s3) == True:
    print ('yes')
if is_valid_triangle (s1, s2, s3) == False:
    print ('no')
