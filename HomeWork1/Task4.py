# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).


from random import randint 
N = randint(1, 4) # как вызвать эту команду загуглено в интернете
print(f"Сгенерирована четверть {N}")
if (N == 1):
    print(f"У четверти {N} диапазон возможных координат - X [0, +оо], Y [0, +оо]")
elif (N == 2):
    print(f"У четверти {N} диапазон возможных координат - X [-oo, 0], Y [0, +oo]")
elif (N == 3):
    print(f"У четверти {N} диапазон возможных координат - X [-oo, 0], Y [-oo, 0]")
elif (N == 4):
    print(f"У четверти {N} диапазон возможных координат - X [0, +оо], Y [-oo, 0]")