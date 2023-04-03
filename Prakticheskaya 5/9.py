import random
mass = []
n = int(input())
for i in range(n):
    mass.append('0')
mass.insert(3, 1)
mass.append(1)

print(mass)


'''
import random
n = int(input())
mass = [0] * n
count = 2
while count != 0:
    pos = random.randint(0, len(mass))
    if mass[pos] != 1:
        mass[pos] = 1
        count -= 1
print(mass)
'''
