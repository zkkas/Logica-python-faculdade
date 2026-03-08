pecascodigo1 = input("codigo peça: ") #entrada de dados do codigo da peça
pecasunidade1 = int(input("unidade: ")) #entrada de dados da unidade
pecasvalor1 = float(input("valor: ")) #entrada de valor da unidade

pecascodigo2 = input("codigo peça: ") #entrada de dados do codigo da peça2
pecasunidade2 = int(input("unidade: ")) #entrada de dados da unidade 
pecasvalor2 = float(input("valor: ")) #entrada de valor da unidade

calculo = (pecasunidade1 * pecasvalor1) + (pecasunidade2 * pecasvalor2) #calculo do total das peças 1 e peças 2

print(f"R$: {calculo:.2f}") #printa o valor total do calculo