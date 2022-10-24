# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#  многочлена и записать в файл многочлен степени k.

#  Пример:

# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
k = int(input('Введите натуральную степень k = '))
list = [] 
for i in range(k+1):
    list.append(randint(0, 100))
result = []
for i in range(k,-1,-1):
    if list[i] != 0:
        if i == 0:
            result.append(f'{list[i]}')
        elif i == 1:
            result.append(f'{list[i]}*x')
        else:
            result.append(f'{list[i]}*x^{i}')
with open ('HomeWork4\\file.txt', 'w') as data:
    data.write(" + ".join(result) + " = 0")    