# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов,
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
# **Вывод:** Парам пам-пам

text = 'пара-ра-рам рам-пам-папам па-ра-па-да'

print('Парам пам-пам' if len(set((map(lambda x: len(
    [i for i in x if i in 'ауоеияюэы']), (text.lower()).split(' '))))) == 1 else 'Пам парам')

#  c filter()
print('Парам пам-пам'if len(set((map(lambda x: len(list(filter(lambda i: i in 'ауоеияюэы', x))),
      (text.lower()).split(' '))))) == 1 else 'Пам парам')


# text = input().lower().split()
# vowels = 'аеоуюёэяи'
# result = set()
# for word in text:
#     count = 0
#     for i in word:
#         if i in vowels:
#             count += 1
#     result.add(count)

# if len(result) == 1:
#     print("Парам пам-пам")
# else:
#     print("Парам пам")
