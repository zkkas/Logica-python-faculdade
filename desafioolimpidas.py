a0,a1,a2 = map(int, input().split())

if ((a0 >= min(a1,a2)) and (a0 <= max(a1, a2))):
    print(a0)
elif ((a1 >= min(a0, a2)) and (a1 <= max(a0,a2))):
    print(a1)
elif ((a2 >= min(a0,a1)) and (a2 <= max(a0,a1))):
    print(a2)