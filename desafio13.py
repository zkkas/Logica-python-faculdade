def  Maior(a, b):
    return int((a +b + abs (a-b)) / 2)

a,b,c = map(int, input().split())

print(f'{Maior(Maior(a,b), c )}')