# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai.Последняя строка содержит число X


list =[i for i in range (1,int(input("Введите размер списка: "))+1)]
print(list, f' - {list.count(int(input("Введите число для поиска: ")))}  раз')


# n = int(input("Введите кол-во элементов: "))
# array = [int(i) for i in input("Введите значения массива: ").split()]
# x = int(input("Введите число, которое нужно подсчитать: "))
# count = 0
# for el in array: #for el in range(n):
#     if el == x:  #if array [el] == x:
#         count += 1
# print(count)



