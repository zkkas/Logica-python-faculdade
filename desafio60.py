Numeros = [float(input()) for i in range(6)]
positivo = len([i for i in Numeros if i > 0])
print('{} VALORES POSITIVOS'.format(positivo))