Lados = input().split()

a,b,c = sorted(map(float, Lados), reverse=True)

if a >= (b + c):
    print('NAO FORMA TRIANGULO')
else:
    if a**2 == b**2 + c**2:
        print('TRIANGULO RETANGULO')
    elif a**2 > b**2 + c**2:
        print('TRIANGULO OBTUSANGULO')
    elif a**2 < b**2 + c**2:
        print('TRIANGULO ACUTANGULO')

lados = [a,b,c]

if len(set(lados)) == 1:
        print('TRINAGULO EQUILATERIO')
elif len(set(lados)) == 2:
        print('TRIANGULO ISOSCELES')
