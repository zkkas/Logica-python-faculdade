numero = int(input("Digite o seu numero: ")) #aqui eu defino a variavel numero pra um inteiro com uma entrada de dados
horas = int(input("Digite o número de horas: "))#aqui eu defino a variavel horas pra um inteiro com uma entrada de dados
valorhora = float(input("Digite o total que recebe por hora: "))#aqui eu defino a variavel valorhora pra um inteiro com uma entrada de dados
soma = horas * valorhora # aqui eu faço o calculo das horas trabalhadas e o valor que o funcionario recebe por hora dentro da variavel soma.

print(f"NUMBER:{numero}") # aqui eu printo o numero do funcionario chamando a variavel numero que foi digita pelo usario antes
print(f"SALARY = U${soma:.2f}") # aqui eu printo o salario do funcionario que anteriomente foi feita a soma na variavel soma assim eu chamo a variavel soma.