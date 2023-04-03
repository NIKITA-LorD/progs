a = 'abcdeftr'
b = ''.join(sorted(a))
mass = []
for i in range(len(a)):
    for i in range(len(b)):
        if a[i] != b[i]:
            mass.append(str(b[i]))
            break
        elif a[i] == b[i]:
            mass.append('yes')

print(mass[-1])




