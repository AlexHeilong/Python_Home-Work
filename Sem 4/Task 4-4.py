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

from random import randint as rI
def creatCoef():
    degree = int(input('Введите максимальную степень: '))
    coef = {}
    for i in range(degree, -1, -1): 
        coef[i] = rI(-20, 20) 
    return coef
coefEquation = creatCoef()
print(coefEquation)

def crateEquation(coefEquation: dict):
    equation = ' '
    first = True
    for i in coefEquation.items():
        if first: 
            first = False 
            if i[1] < 0:
                equation += ' - ' + str(abs(i[1])) + 'x^' + str(i[0])
            elif i[1] > 0:
                equation += str(abs(i[1])) + 'x^' + str(i[0])
        else:
            if i[1] < 0:
                equation += ' - ' + str(abs(i[1])) + 'x^' + str(i[0])
            elif i[1] > 0:
                equation += ' + ' + str(abs(i[1])) + 'x^' + str(i[0])
    return equation + ' = 0'
a = crateEquation(coefEquation)
print(a)