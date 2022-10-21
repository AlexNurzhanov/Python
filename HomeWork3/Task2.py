# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.
#  Пример:

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]


list1 = [2, 3, 4, 5, 6]
list2 = [2, 3, 5, 6]
def multy(pair): 
    result = [] 
    for i in range(len(pair)):
        if(i <= len(pair) - i - 1): 
            result.append(pair[i] * pair[len(pair) - i - 1])
    return result
print(f'Произведение пар списка - {list1} = {multy(list1)}')
print(f'Произведение пар списка - {list2} = {multy(list2)}')