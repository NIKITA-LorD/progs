a = input()
z = 0
for i,s in enumerate(a):
    if s.isdigit():
        z+= len(s)

print(z)








'''a = input()
z = 0
for i in a:
    if isinstance(a[i], int):
        z += 1
    else:
        i+=1
print(z)'''