# Задача №17. Общее обсуждение
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.


# list_1 = [1,1,2,0,-1,3,4,4]
# print(f'{len(set(list_1))} различных чисел')

n =[ int(i) for i in input().split()]
n = set(n) 
print(len(n))