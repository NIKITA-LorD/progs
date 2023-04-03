mass = []
a = int(input('Длина? - '))
b = -1


for i in range(a):
    if len(mass) == a:
        print(mass)
    else:
        b += 2
        mass.append(b)

print(mass)








