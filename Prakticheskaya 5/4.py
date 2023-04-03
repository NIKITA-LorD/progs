a, b = map(int, input('Введите первый элемент и разность прогрессии через пробел -').split())
n = 10
c = []
c.append(a)
for i in range(n+1):
   
    if i != n:
        c.append(a+b)
        a = a + b
    else:
        break
print(c)








