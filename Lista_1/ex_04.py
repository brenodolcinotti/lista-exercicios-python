n1=float(input('Digite o valor total da compra: '))

print(n1)

if n1 <= 100:
    print('Não possuem desconto')

elif n1 > 100 and n1 <= 300:
    res10 = n1 / 10
    des10 = n1 - res10 
    print('Valor do desconto de 10%: ', res10)
    print('Valor a pagar: ', des10)

else:
    res20 = n1 / 5
    des20 = n1 - res20 
    print('Valor do desconto de 20%: ', res20)
    print('Valor a pagar: ', des20)