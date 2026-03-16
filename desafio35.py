a,b,c,d = map(int, input('').split())
somac = c + d
somaa = a + b
if b > c and  d > a and somac > somaa and c > 0 and d > 0 and a % 2 == 0:
    print("valores aceitos")
else:
    print('valores não aceito')

