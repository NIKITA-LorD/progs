n = [2,3,354,4567,56763,123,12,325]
summ = 0
proizw = 1
for i in range(len(n)):
    if n[i] != len(n):
        summ += n[i]
        proizw *= n[i]
print(summ, proizw)




