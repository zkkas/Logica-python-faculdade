codigo, quantidade = map(float, input().split())
precos= {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50,
    6: 3.00,
}
def calcular(codigo,quantidade):
    precos_unitario = precos.get(codigo, 0.0)
    return precos_unitario * quantidade

resultado = calcular(codigo, quantidade)
print(f'Total: R$:{resultado:.2f}') 