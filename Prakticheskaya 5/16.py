n = [2,3,354,4567,56763,123,12,325]

a = 0
for i in range(len(n)):
    if (n[i]%2 != 0) and (n[i] < 11):
        a += n[i]
print(a)







