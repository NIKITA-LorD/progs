mass = []
a = int(input('Длина? - '))
b = 1


for i in range(a):
    if len(mass) == a*3:
        print(mass)
    else:
        mass.append(str(b))
        mass.append(str(b))
        mass.append(str(b))
        b += 1

print(mass)






