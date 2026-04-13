Diaa = int(input().split(" ")[1])
HoraA, MinutoA, SegundoA = map(int, input("").split(' : ')[1])

DiaB = int(input().split(" ")[1])
Horab, MinutoB, SegundoB = map(int, input("").split(' : ')[1])

segundos = (SegundoB - SegundoA) % 60

segundoMaior = SegundoA > SegundoB
Minutos = (MinutoB - MinutoA - int(segundoMaior)) % 60

minutomaior= MinutoA > MinutoB
Horas = (Horab - HoraA - (int(segundoMaior) or  int(minutomaior))) % 24

HoraMaior = HoraA > Horab
Dias = (DiaB - Diaa - int(segundoMaior)) or int (minutomaior) or int(HoraMaior)

print(f'{Dias} dia(s)')
print(f'{Horas} hora(s)')
print(f'{Minutos} minuto(s)')
print(f'{segundos} segundo(s)')