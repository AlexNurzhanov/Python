# Вычислить число c заданной точностью d
#  Пример:

# при d = 0.001, π = 3.141.  10-1 ≤ d ≤10-10
# π = (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + (4/13) - (4/15) ...


import math
from math import pi

d = input('Введите заданную точность, d: \n').count('0')
print(f'Число π с заданной точностью {d} = {round(pi,d)}')