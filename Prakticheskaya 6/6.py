
def F():
    b = ''
    for i in range(len(a)):
        if i % 2 != 0:
            b += '0'
        else:
            b += str(a[i])
    print(b)
a = input('Введи пятизначное число - ')
F()
    




