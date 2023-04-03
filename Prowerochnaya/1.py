a = int(input('Введите длину первого катета - '))
b = int(input('Введите длину второго катета - '))
import math
S = a*b/2
#S = int(S)
G = math.sqrt(a**2 + b**2)
P = a+b+G
print(f'Площадь вашего треугольника {round(S, 2)}')
print(f'Периметр вашего треугольника {round(P, 2)}')
print(f'Гипотенуза вашего треугольника {round(G, 2)}')

