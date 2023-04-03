f = open('RabFiles/2file.txt', 'r+')
stroka = f.readline()
stroka = stroka.split(' ')
new_string = []
q,w,e,r,t,y,u,i,o,p = '1','2','3','4','5','6','7','8','9','0'
for elem in stroka:
    if (q not in elem) and (w not in elem) and (e not in elem) and (r not in elem) and (t not in elem) and (y not in elem) and(u not in elem) and(i not in elem) and (o not in elem) and (p not in elem):
        new_string.append(elem)
f.close()

f = open('RabFiles/1file.txt', 'w')
new_string = ' '.join(new_string)
print(new_string)

f.write(new_string)
f.close()



'''f = open('RabFiles/2file.txt', 'r+')
stroka_mass = f.readline()
stroka = stroka_mass.split(' ')
stroka = list(stroka)
new_string = []
def proverka(word):
    for elem in word:
        a = []
        a.append(elem)
        for elem in a:
            if type(elem) != int:
                return True
            else:
                return False

for elem in stroka:
    if proverka(elem) == True:
        new_string.append(elem)
f.close()

f = open('RabFiles/1file.txt', 'w')
new_string = ' '.join(new_string)
print(new_string)

f.write(new_string)
f.close()'''
