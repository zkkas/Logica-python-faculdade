cd, p1, pv1 = map(float, input("").split())
cd2, p2, pv2 = map(float, input("").split())
calculo = (p1 * pv1) + (p2 * pv2) #calculo do total das peças 1 e peças 2
print(f"R$: {calculo:.2f}") #printa o valor total do calculo