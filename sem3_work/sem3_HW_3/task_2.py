# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X


n = (int(i) for i in input("Введите размер списка: "))
a = [int(i) for i in input('Введите числа через пробел: '). split()]
x = int(input('Введите число X, с которым необходимо сравнивать элементы списка: '))
min_el = abs(x - a[0])
index = 0
for i in range(len(a)):
        count = abs(x - a[i])
        if count < min_el:
            index = i
print(f'Число {a[index]} в списке самое близко по величине к числу {x}.')
# print(f'Число {a[index]} в списке самое близко по величине к числу {x}.Их разница составляет {abs(x - a[index])}')



