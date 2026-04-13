DDD = int(input())

cidades = {
    61: "Brasilia",
    71: "Salvador",
    11: "Sao Paulo",
    21: "Rio De Janeiro",
    32: "Juiz De fora",
    19: "Campinas",
    27: "Vitoria",
    31: "Belo Horizonte",
}

def pegar(codigo):
    valor = cidades.get(codigo)
    return valor

resultado = pegar(DDD)
print(resultado)