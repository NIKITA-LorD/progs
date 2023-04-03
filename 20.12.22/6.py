c = 0
a1 = ''
for i in range(1,11):
    c += i**i
    a1 += str(i) * i
a = reversed(a1)
print(a1)
print("Сумма:", c)

