a = 'ggkngn 5154 15 11 35 f 51g e51gdgijge f ei gig eg 8eg eg 8g8 8eg 868g46e 84 8 jo'
a = ''.join(a)
mass = []
r = ['0','1','2','3','4','5','6','7','8','9']
for i in range(len(a)):
    if (a[i] in r) or a[i] == ' ':
        if a[i] in r and a[i+1] in r:
            mass.append(a[i])



print(mass)
