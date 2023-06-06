# Задача №35.
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def prime(n):
    i = 2
    flag = True
    while i < n // 2 + 1 and flag:
        if n % i == 0:
            flag = False
        i += 1
    if flag:
        return 'yes'
    return 'no'


print(prime(int(input())))

  

##   2 вариант 


# a = int(input("Введите число: "))
# k = 0
# for i in range(2, a // 2 + 1):
#     if (a % i == 0):
#         k = k + 1
# if (k <= 0):
#     print("Число простое")
# else:
#     print("Число не является простым")
