# Задача №43. 
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод:              Вывод:
# 1 2 3 2 3                 2
list_1 = [int(i) for i in input().split()]
count = 0
for i in range(len(list_1)):
    for j in range(i + 1, len(list_1)):
        if list_1[i] == list_1[j]:
            count += 1
print(count)


# решение через словарь: 


n = int(input())
list_1 = [int(i) for i in input().split()][:n]
count = 0
result = {}
for i in list_1:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1
print(sum([i // 2 for i in result.values()]))