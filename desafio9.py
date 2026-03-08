nome = input("Qual e o seu nome: ") #entrada de dados do nome
salario = float(input("Qual e o seu salario: ")) #entrada de dados do salario do tipo float
vendas = float(input("Informe o seu total de vendas: ")) #entrada de dados de vendas do tipo float

total =  salario + (vendas* 0.15 ) # variavel total que faz o calculo que o funcionario deve receber 

print(f"R$: {total:.2f}") #printa o total que o funcionario deve receber
