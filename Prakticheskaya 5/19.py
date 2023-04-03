n = [3, 2, 6, 9, 4, 8, 7]
a = 0
for i in range(len(n)):
    if (i+1) %2 != 0 and n[i] < n[0] + n[-1]:
        a += n[i]


print(a)

