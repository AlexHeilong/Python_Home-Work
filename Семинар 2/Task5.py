# Реализуйте алгоритм перемешивания списка.
import random
list = [random.randint(-10,10) for i in range(random.randint(5,20))]
print(f"Стартовый список:\n {list}")
random.shuffle(list)
print(f"Перемешенный список:\n{list}")