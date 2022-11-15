# Улучшение HomeWork2. Task1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# было
# number = input("Введите вещественное число: ")
# sum = 0
# for i in number:
#     if i != '.':
#         sum += int(i)
# print(sum)

#стало
number = lambda x: sum([int(it) for it in str(x) if "0" <= it <= "9"])
print(number(-6782))