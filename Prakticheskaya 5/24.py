n = [3, 2, 6, 9, 4, 8, 7]
a = []

for i in range(len(n)):
    if (i+1) % 2 != 0 and n[i]%3 == 0:
        a.append(n[i])
print(max(a))





