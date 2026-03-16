N = int(input())

Horas = N//3600
N = N%3600
Minutos = N/60
N = N%60

print('{}: {:.0f}: {}'.format(Horas,Minutos,N))