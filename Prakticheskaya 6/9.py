def F():
    c = ''
    for i in range(len(a)):
        if int(a[i]) < 5:
            c += str(a[i])
    for i in range(len(a)):
        if int(a[i]) >= 5:
            c += str(a[i])
    print(c)
a = input("Введите четырёхзначное число - ")
F()





