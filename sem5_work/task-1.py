# Задача №31.
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где a0 = 0, a1 = 1,
# ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 13
# Задание необходимо решать через рекурсию


def fib(n):

    if n == 0 or n == 1:
        return n

    return fib(n - 1) + fib(n - 2)

print(fib(int(input())))



##  2 вариант: 

# fib1 = 1
# fib2 = 1

# n = int(input("Номер элемента ряда Фибоначчи: "))

# i = 0
# while i < n - 2:
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     i = i + 1

# print("Значение этого элемента: ", fib2)



