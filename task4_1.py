# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
#
# 6 12


n = int(input("Введите длину массива: "))
d = int(input("Ввудите длину массива: "))
arr1 = set()
arr2 = set()

for i in range(n):
    arr1.add(int(input("Введите элемент 1го массива:")))
print()
for i in range(d):
    arr2.add(int(input("Введите элемент 2го массива:")))

result_set = set.intersection(arr1, arr2)
print(result_set)