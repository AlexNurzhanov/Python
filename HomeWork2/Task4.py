# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.


from random import randint


def makeList(N):
    
    #Функция создает список из n - случайных элементов промежутка [-N, N].
    
    listNum = []
    for i in range(N):
        listNum.append(randint(-1 * N, N))
    return listNum


def findMult(list_n):
    
    #Функция находит произведение элементов списка находящихся на позициях заданых в текстовом файле.
    
    file = open('HomeWork2\\file.txt', 'r')
    Lines = file.readlines()
    mult = 1
    for line in Lines:
        mult *= list_n[int(line)]
    return mult


list1 = makeList(10)
print(list1)

multListEl = findMult(list1)
print(f'произведение элементов на указанных позициях (file.txt) = {multListEl}')