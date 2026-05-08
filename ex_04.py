def registrar_entrada(estoque, quantidade):
    novo_estoque = estoque + quantidade
    print(f"Entrada de {quantidade} unidade(s) registrada com sucesso!")
    return novo_estoque

def registrar_saida(estoque, quantidade):
    if quantidade > estoque:
        print(f"Erro: Saldo insuficiente. Você tentou retirar {quantidade}, mas só há {estoque} no estoque.")
        return estoque
    else:
        novo_estoque = estoque - quantidade
        print(f"Saída de {quantidade} unidade(s) registrada com sucesso!")
        return novo_estoque

def exibir_estoque(estoque):
    print(f"Saldo atual em estoque: {estoque} unidade(s).")


print("--- Sistema de Controle de Estoque ---")

while True:
    try:
        estoque_atual = int(input("Informe a quantidade inicial em estoque: "))
        if estoque_atual >= 0:
            break
        else:
            print("O estoque inicial não pode ser negativo.")
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")

exibir_estoque(estoque_atual)

while True:
    print("\n" + "="*30)
    print("1 - Registrar Entrada")
    print("2 - Registrar Saída")
    print("3 - Exibir Estoque")
    print("0 - Sair")
    
    opcao = input("Escolha uma operação: ")
    print("-" * 30)
    
    if opcao == '1':
        try:
            qtd = int(input("Digite a quantidade para ENTRADA: "))
            if qtd > 0:
                estoque_atual = registrar_entrada(estoque_atual, qtd)
                exibir_estoque(estoque_atual)
            else:
                print("A quantidade deve ser maior que zero.")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")
            
    elif opcao == '2':
        try:
            qtd = int(input("Digite a quantidade para SAÍDA: "))
            if qtd > 0:
                estoque_atual = registrar_saida(estoque_atual, qtd)
                exibir_estoque(estoque_atual)
            else:
                print("A quantidade deve ser maior que zero.")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")
            
    elif opcao == '3':
        exibir_estoque(estoque_atual)
        
    elif opcao == '0':
        print("Encerrando o sistema de estoque. Até logo!")
        break
        
    else:
        print("Opção inválida. Escolha um número de 0 a 3.")