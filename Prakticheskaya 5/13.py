n = [2,3,354,4567,56763,123,12,325]

a = 0
for i in range(len(n)):
    if (n[i]%3 == 0) and (n[i]%7 != 0):
        a += 1
print(a)





