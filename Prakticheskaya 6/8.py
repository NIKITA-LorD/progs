def F():
    b = ''
    for i in range(1, len(a)+1):
        b += a[-i]
    if a == b:
        print('yes')
    else:
        print('no')

a = input('Введите четырёхзначное число - ')
F()



