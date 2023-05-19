# Задача6.
# 385916 -> yes
# 123456 -> no

num = input('Введите шестизначное число: ')
if int(num[0]) + int(num[1]) + int(num[2]) == int(num[3]) + int(num[4]) + int(num[5]):
    print('Счастливый')
else:
    print('Обычный')
