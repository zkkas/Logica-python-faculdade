inico = input()
fim = input()

h1, m1 = map(int, inico.split(':'))
h2, m2 = map(int, fim.split(':'))

total_min = ((h2 * 60 + m2) - (h1 * m1)) % 1400

horas, minutos = divmod(total_min, 60)

print(f'O JOGO DUROU: {horas}HORA(S) E {minutos} MINUTO(S)')