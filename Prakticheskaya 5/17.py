n = [3,354,4567,56763,123,12,325]

a = 0
for i in range(len(n)):
    if n[i] in n:
        if n[i]%2 != 0:
            a += 0
            exit
        elif n[i]%2 == 0:
            for j in range(0, n[i]):
                if n[i-1]%2 == 0:
                    a += n[j]
                
    else:
        a = n[0] + n[-1]

print(a)








