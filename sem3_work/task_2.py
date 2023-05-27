# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число K.
#  Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо,
# K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.


# list_1 = [int(i) for i in input('Введите числа через пробел2: '). split()]
# step = int(input('Введите кол-во сдвигов: '))
# result_list =[list_1[i - step] for i in range(len(list_1))]
# print(result_list)


#                                    2 вариант

list_1 = [int(i) for i in input('Введите числа через пробел: '). split()]
step = int(input('Введите кол-во сдвигов: '))
step = step % len(list_1)
result_list = list()
for i in range(len(list_1)):
    result_list.append(list_1[i - step])
print(result_list)
