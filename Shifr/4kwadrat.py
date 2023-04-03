import random
import re

def create_kvadrat():
    alfavit = []
    counter = 0
    temp_mass = []
    for i in range(ord('A'), ord('Z')+1):
        temp_mass.append(chr(i))
        counter += 1
        if counter >= 5:
            random.shuffle(temp_mass)
            alfavit.append(temp_mass)
            temp_mass = []
            counter = 0
    random.shuffle(alfavit)
    return alfavit

kvadrat = {'mass_1':create_kvadrat(), 'mass_2':create_kvadrat(),
           'mass_3':create_kvadrat(), 'mass_4':create_kvadrat()}

#отобразить квадрат
for i in range(5):
    print(f"{kvadrat['mass_1'][i]} | {kvadrat['mass_2'][i]}")
print('-----------------------------------------------------')
for i in range(5):
    print(f"{kvadrat['mass_3'][i]} | {kvadrat['mass_4'][i]}")

sycret = 'somebodygivethisguyaguns' 
new_string = ''

mass_sycret = re.findall(r'([a-z])([a-z])', sycret)

print(mass_sycret)

for elem in mass_sycret:
    for chek_mass in kvadrat['mass_1']:
        if elem[0].upper() in chek_mass:
            first_index = chek_mass.index(elem[0].upper())
            first_row = kvadrat['mass_1'].index(chek_mass)
    for chek_mass in kvadrat['mass_4']:
        if elem[1].upper() in chek_mass:
            second_index = chek_mass.index(elem[1].upper())
            second_row = kvadrat['mass_4'].index(chek_mass)

    new_string += kvadrat['mass_3'][second_row][first_index]
    new_string += kvadrat['mass_2'][first_row][second_index]
    new_string += ' '

print(new_string)





