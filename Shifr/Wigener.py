def code():
    mass = []
    end_count_chr = 25
    start_count_chr = 0
    unicode_start_index = 97


    while start_count_chr <= end_count_chr:
        temp = []
        for i in range(ord('a'), ord('z')+1):
            temp.append(chr((i + start_count_chr - unicode_start_index) % 26 + unicode_start_index))
        mass.append(temp)
        start_count_chr += 1



    base_alf = []
    for i in range(ord('a'), ord('z')+1):
        base_alf.append(chr(i))
    
    return mass

def code_print():
    mass = []
    end_count_chr = 25
    start_count_chr = 0
    unicode_start_index = 97


    while start_count_chr <= end_count_chr:
        temp = []
        for i in range(ord('a'), ord('z')+1):
            temp.append(chr((i + start_count_chr - unicode_start_index) % 26 + unicode_start_index))
        mass.append(temp)
        start_count_chr += 1

    base_alf = []
    for i in range(ord('a'), ord('z')+1):
        base_alf.append(chr(i))

    # Вывод
    print(' ', end=' ')
    for elem in base_alf:
        print(elem, end=' ')
    print()
    print('--------------------------------------')

    for i in range(0, len(mass)):
        print(base_alf[i], end='|')
        for e in mass[i]:
            print(e, end=' ')
        print()

code_print()

