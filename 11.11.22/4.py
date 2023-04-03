a = range(10)
c = " "
for i in range(0,10):
    if a[i] % 2 == 0:
        c += "A"
    else:
        c += str(int(a[i] + 1))

print(c)

