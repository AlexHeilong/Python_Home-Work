# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from operator import ne
import random
from re import X
num = int(input("Введите число: "))
myList = []
for i in range(num):
    myList.append(random.randint(0, num))
print(myList)
print('-')

newList = []
for i in range((len(myList)+1)//2):
    newList.append(myList[i]*myList[len(myList)-1-i])
print(newList)

