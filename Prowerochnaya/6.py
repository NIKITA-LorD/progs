import math
 
print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
 
discr = b ** 2 - 4 * a * c
print("Дискриминант =", discr)
 
if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 =", x1)
    print("x2 =", x2)
elif discr == 0:
    x = -b / (2 * a)
    print("x =", x)
else:
    print("Корней нет")







'''a = int(input('Введите коэффициент "a": '))
b = int(input('Введите коэффициент "b": '))
c = int(input('Введите коэффициент "c": '))

F = a*x**2 + b*x + c

for x in range():
    if F == 0:
        print("x =", x)'''