distancia = float(input("Digite a distância percorrida em km: "))
consumo = float(input("Digite o consumo médio do veículo em km/l: "))
preço_combustivel = float(input("Digite o preço do combustível/l em reais: "))
orcamento = float(input("Digite o orçamento disponível para a viagem em reais: "))

# Quantidade de litros necessários:
litros_necessarios = distancia / consumo

# Valor total do combustível:
valor_total = litros_necessarios * preço_combustivel

if valor_total <= orcamento:
    print("Viagem Autorizada!")

elif valor_total > orcamento:
    print("Viagem Não Autorizada. Orçamento insuficiente.")