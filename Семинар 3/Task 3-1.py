# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
#  - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
num = int(input("Введите число: "))
myList = []

for i in range(num):
    myList.append(random.randint(0, num))
print(myList)

sum = 0
for i in range(1, num+1, 2):    
    sum = sum + myList[i]

print(f'Сумма элементов на нечетных индексах равна {sum} ')    






# exit()
# newList = []
# i = 0
# while i < len(myList):
#     index = random.choice(range(len(myList)))
#     newList.append(myList[index])
#     myList.pop(index)
# print(newList)