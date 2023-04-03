f = open('RabFiles/1file.txt', 'r')
stroka = f.readline()
stroka = stroka.split(' ')
print(stroka)

new_string = []

for elem in stroka:
    if int(elem) % 2 != 0:
        new_string.append(elem)
f.close()

f = open('RabFiles/1file.txt', 'w')
new_string = ' '.join(new_string)
print(new_string)

f.write(new_string)
f.close()

