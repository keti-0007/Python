# Задача.15


n = int(input("Введите число: "))
max_massa = 0
min_massa = 1000
for i in range(n):
    x = int(input("Введите массу арбуза: "))
    if x > max_massa:
        max_massa = x
    elif x < min_massa:
        min_massa = x
print(min_massa, max_massa)