positivos = []
for i in range(6):
    numero = float(input())

    if numero > 0 :
        positivos.append(numero)
    
print(f'{len(positivos)} valores positivos \n {(sum(positivos)/len (positivos)):.1f}')
