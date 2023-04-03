a = []

for i in range(1,11):
    if i%2 == 0:
        a.append(str(i))
    else:
        a.append("A")

s = ''.join(a)

print(s)







