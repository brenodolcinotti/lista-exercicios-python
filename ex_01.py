n1=int(input('Insira sua idade '))

if n1 < 0:
    print('Por favor inserir uma idade válida')

elif n1 >= 0 and n1 <= 12:
    print('Criança')

elif n1 >= 13 and n1 <= 17:
    print('Adolescente')

elif n1 >= 18 and n1 <= 59:
    print('Adulto')

else:
    print('Idoso')
