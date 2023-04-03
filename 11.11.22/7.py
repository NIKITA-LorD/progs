s = '0=456-=+430-64=36+-464y-053yv+gy=0-v4=5y'

c = s.count("-")
d = s.count("+")
k = c + d
print(f"Количество '+' и '-' = {k}")

ar = [char for char in s]
#print(ar)
w = 0
t = "0"
y = []

for i in s:
    if ((i == "+" ) or (i == "-")) and i+1 == "0":
        w =+ 1
    print(w)











