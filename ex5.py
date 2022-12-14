import math

x1 = int(input('Введите х1'))
y1 = int(input('Введите у1'))
x2 = int(input('Введите x2'))
y2 = int(input('Введите y2'))

dist = ((x2-x1)**2)+((y2-y1)**2)
answer = math.sqrt(dist)

print(answer)