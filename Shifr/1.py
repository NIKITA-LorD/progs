import random
import re

def create_kvadrat():
    alfavit = []
    counter = 0
    temp_mass = []
    for i in range(ord('А'), ord('Я')+1):
        temp_mass.append(chr(i))
        counter += 1
        if counter >= 8:
            random.shuffle(temp_mass)
            alfavit.append(temp_mass)
            temp_mass = []
            counter = 0
    random.shuffle(alfavit)
    return alfavit

kvadrat = {'mass_1':create_kvadrat(), 'mass_2':create_kvadrat(),
           'mass_3':create_kvadrat(), 'mass_4':create_kvadrat()}

#отобразить квадрат
for i in range(4):
    print(f"{kvadrat['mass_1'][i]} | {kvadrat['mass_2'][i]}")
print('-----------------------------------------------------')
for i in range(4):
    print(f"{kvadrat['mass_3'][i]} | {kvadrat['mass_4'][i]}")






