a = 'ехал|грека.через,реку'
b = ',|.'
a1 = list(a)
b1 = list(b)

c= []
for i in range(len(a1)+1):
    if a1[i] not in b1:
        c = c.append(a1[0:i])
        print(c)
        c = a1.remove(a1[0:i])
    else:
        i += 1




















"""for index in range(len(a)):
        if a[index] in b:
            mass.append(a[0:index])
            a = a.replace(a[0:index], '')
            print(a)




def sas(a):
    for index in range(len(a)):
        if a[index] in b:
            mass.append(a[0:index])
            a = a.replace(a[0:index], '')
            print(a)

while len(a)>0:
    sas(a)
    mass = mass.remove(a[0:index])



print(mass)


# c = []
# c.append(a)

# n = []
# n.append(b)


# for i in range(len(a)+1):
#     for j in range(len(a)+1):
#         if c[i]+n[j] == c[i]+c[i+1]:
#             print(c[0:i])
#             c = c.remove(c[0:j])
"""