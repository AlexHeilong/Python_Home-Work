
# Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего
# на 1 меньше и так до ноля
# Коэффициенты расставляет random,
# поэтому при коэффициенте 0 просто пропускаем данную итерацию степени
# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0
import random
from random import randint
num = 0
def koef_dict(number):
    num = int(input('Введите степень: '))
    koefDict = {}
    for i in range(num, -1, -1):
        koefDict[i] = random.randint(-100, 100)
    return koefDict
z = koef_dict(num)
print(z)

def my_equation(my_dict: dict):
    equation = ' '
    first = True
    for i in my_dict.items():
        if first == False:
            if i[1] < 0:
                equation += '-' + str(abs(i[1])) + 'x^' + str(i[0])
            elif i[1] > 0:
                equation += str(abs(i[1])) + 'x^' + str(i[0])
        else:
            if i[1] < 0:
                equation += '-' + str(abs(i[1])) + 'x^' + str(i[0])
            elif i[1] > 0:
                equation += '+' +  str(abs(i[1])) + 'x^' + str(i[0])

    return equation + '= 0'

e = my_equation(z)
print(e)

