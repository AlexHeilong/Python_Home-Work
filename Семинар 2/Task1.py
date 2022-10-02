# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

num = float(input("Введите число: "))
sum = 0
if num < 0:
    num *= (-1)
if num != int(num):
    num = num * 10
while num > 0:
    sumOfNum = num % 10
    sum = sum + sumOfNum
    num = num // 10
print(f'Сумма цифр равна {sum}')


