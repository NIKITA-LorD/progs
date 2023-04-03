a, b, c, d = map(int, input("Введите 4 числа через пробел - ").split())

mass = []
mass.append(a)
mass.append(b)
mass.append(c)
mass.append(d)
mass_1 = []
for i in mass:
    if i % 2 == 0:
        mass_1.append(i)
if len(mass_1) == 0:
    print("not found")
if len(mass_1) != 0:
    print('Наибольшее четное число: ', max(mass_1))


