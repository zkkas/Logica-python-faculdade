n1,n2,n3,n4 = map(float, input().split())
media = ( n1 * 2  + n2 *3 + n3 * 4 + n4 * 1 ) / 10

if media >=  7:
    print(f"Media: {media:.1f}")
    print('Aluno Aprovado')

elif media > 5:
    print('Aluno em Exame')
    nota = float(input(''))
    print(f"Nota Do Exame {nota}")
    mediafinal = (media + nota) / 2

    if mediafinal >= 5: 
        print('Aluno Aprovado')
        print(f'Media final: {mediafinal:.1f}')
    else:
        print('Aluno reprovado')
        
else:
    print(f"Media: {media:.1f}")
    print('Aluno Reprovado')