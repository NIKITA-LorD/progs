a = input()

if len(a)>5:
    print(a[:3], a[-3::1])
else:
    print(a[1]*len(a), sep=" ")




