import random
import re
from Wigener import code
from Wigener import code_print



kvadrat = {'mass_1':code(), 'mass_2':code(),
           'mass_3':code(), 'mass_4':code()}

#отобразить квадрат
for i in range(26):
    print(f"{kvadrat['mass_1'][i]} | {kvadrat['mass_2'][i]}")
print('-----------------------------------------------------')
for i in range(26):
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








