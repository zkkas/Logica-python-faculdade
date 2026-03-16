from math import sqrt 
a,b,c = map(float, input().split())

deltas = (b**2) - 4*a*c

if deltas > 0 and a != 0:
    R1 = (-b + sqrt(deltas)) / (2*a)
    R2 = (-b - sqrt(deltas)) / (2*a)
    print('R1 = {:.5f}'.format(R1))
    print('R2 = {:.5f}'.format(R2))  
else:
 print('impossivel calcular')