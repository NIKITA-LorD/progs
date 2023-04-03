mass = []
a = int(input('Длина? - '))
b = 0


for i in range(a):
    if len(mass) == a:
        print(mass)
    else:
        b -= 3
        mass.append(b)

print(mass)



