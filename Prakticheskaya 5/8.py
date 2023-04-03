import random
count = random.randint(3,10)
mass = [0] * count

for i in range(count):
    mass[i] = random.randint(0,9)
mass += mass[::-1]

print(mass)






