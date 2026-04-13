filo = input()
classe = input()
alimentacao = input()

if filo == 'vertebrado':
    if classe == 'ave':
        if alimentacao == 'carnivoro':
            print('aguia')
        elif alimentacao == 'onivoro':
            print('pomba')
    elif classe == 'mamifero':
        if alimentacao == 'onivoro':
            print('homem')
        elif alimentacao == 'herbivoro':
            print('vaca')

if filo == 'invertebrado':
    if classe == 'inseto':
        if alimentacao == 'hematofago':
            print('pulga')
        elif alimentacao == 'herbivoro':
            print('lagarta')
    if classe == 'anelideo':
        if alimentacao == 'hematofago':
            print('sanguessuga')
        elif alimentacao == 'onivoro':
            print('minhoca')