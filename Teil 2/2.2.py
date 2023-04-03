'''a = input()

for i in a:
    if ('a' and 'b' and 'c') in a:
        print('Строка содержит только a, b, c')
        break
    else:
        print('-')
        break'''


string = input()

mass = ('a', 'b', 'c')
mass_temp = ['a', 'b', 'c']
chek = False

for elem in string:
    if elem in mass:
        if mass_temp != []:
            mass_temp.remove(elem)
        if mass_temp == []:
            chek = True
    else:
        chek = False
        break

if chek:
    print('Строка содержит только a, b, c!')     
else:
    print('Строка НЕ содержит только a, b, c!')  




