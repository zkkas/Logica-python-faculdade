produtos = []
precos = []
total = 0

while True: 
    carrinho = input("Adicione algo ao carrinho: ")
    if carrinho == "":
        print("valor não pode ser vazio")
        continue
    if carrinho == "sair":
        break
    valor = int(input("Adicione um preço: "))
    if valor == 0:
        print("o valor não foi adicionado")
        continue
    elif valor < 0:
        print("valor menor que 0")
        continue
    else:
        precos.append(valor)
        produtos.append(carrinho)

for n in precos:
    total += n

print(f"quantidades de protudos no carrinho e: {produtos}")
print(f"O total da compra foi: {total}")
print(f"Maximo da compra foi: {max(precos)}")
print(f"Minimo da compra foi: {min(precos)}")
