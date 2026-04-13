i, t = map(int, input().split())

if i >= t:
    print(f'O JOGO DUROU {(24 -i + t)} HORA(S)')
else:
    print(f'O JOGO DUROU {(t - i)} HORA(S)')