
print("Введете номер билет:")
n = int(input())
if n >= 100000 and n < 1000000:
    sum1 = 0
    sum2 = 0
    n1 = n // 1000
    n2 = n % 1000
    while n1 > 0:
        x = n1 % 10
        sum1 = sum1 + x
        n1 = n1 // 10
    while n2 > 0:
        x = n2 % 10
        sum2 = sum2 + x
        n2 = n2 // 10
    if sum1 == sum2:
        print('Yes')
    else:
        print('No')
else:
    print("Нет такой номер билет!")
