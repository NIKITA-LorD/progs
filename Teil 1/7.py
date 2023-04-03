import random

a = ["-", "+", "0"]

stroka = "".join(random.choices(a, k=10))
s = stroka.count('+')
g = stroka.count('-')
t = s + g
#print(stroka)
print("Общее количество '-' и '+' =", t)

z = stroka.count('+0')
x = stroka.count('-0')

print("Количество символов, после которых следует'0' = ", z+x)




