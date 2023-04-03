s = "Дана строка"
c = int(len(s))

for i in range(len(s)):
    if s[i] == s[-1]:
        print(i)
    else:
        i+=1
