# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

list = [1, 1, 2, 3, 4, 5, 4, 3, 2]
print(list)
def newList(list):
    listNew = []
    for i in list:
        if list.count(i) < 2:
            listNew.append(i)
    return listNew
list1 = print(newList(list))

