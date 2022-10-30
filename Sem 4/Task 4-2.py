# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

num = int(input('Введите целое число: '))
simpDevList = []

d = 2
while num > 2:
    if num % d != 0:
        d += 1
    else:
        num //= d
        simpDevList.append(d)
print(simpDevList)

