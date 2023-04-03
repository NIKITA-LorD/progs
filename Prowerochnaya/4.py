a, b, c = map(int, input("Введите 3 числа через пробел - ").split())

summ1 = a+b
summ2 = b+c
summ3 = a+c
S = max(summ1, summ2, summ3)
if S == summ1:
    print("Наибольшая сумма у : ", a, 'и', b, f'({summ1})')
if S == summ2:
    print("Наибольшая сумма у : ", b, 'и', c, f'({summ2})')
if S == summ3:
    print("Наибольшая сумма у : ", a, 'и', c, f'({summ3})')


