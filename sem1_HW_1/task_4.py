# Задача8.

n = int(input('Ширина шоколадки: '))
m = int(input('Длинна шоколадки: '))
k = int(input('Нужное количество долек: '))
if k < n*m and (k % n == 0 or k % m == 0):
    print('Yes')

else:
    print('No')
