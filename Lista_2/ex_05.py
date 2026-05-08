def exibir_menu():
    print("\n" + "="*25)
    print("BANCO DIGITAL - MENU")
    print("1 - Consultar Saldo")
    print("2 - Realizar Saque")
    print("3 - Realizar Depósito")
    print("0 - Sair do Sistema")
    print("="*25)

def consultar_saldo(saldo):
    print(f"\nSeu saldo atual é: R$ {saldo:.2f}")

def realizar_saque(saldo, valor):
    if valor <= 0:
        print("\nErro: O valor do saque deve ser maior que zero.")
        return saldo
    elif valor > saldo:
        print(f"\nErro: Saldo insuficiente para esta operação! Saldo disponível: R$ {saldo:.2f}")
        return saldo
    else:
        novo_saldo = saldo - valor
        print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!")
        return novo_saldo

def realizar_deposito(saldo, valor):
    if valor <= 0:
        print("\n❌ Erro: O valor do depósito deve ser maior que zero.")
        return saldo
    else:
        novo_saldo = saldo + valor
        print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!")
        return novo_saldo


saldo_conta = 0.0

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        consultar_saldo(saldo_conta)

    elif opcao == '2':
        try:
            quantia = float(input("\nDigite o valor que deseja sacar: R$ "))
            saldo_conta = realizar_saque(saldo_conta, quantia)
            consultar_saldo(saldo_conta)
        except ValueError:
            print("\nEntrada inválida! Digite um valor numérico.")

    elif opcao == '3':
        try:
            quantia = float(input("\nDigite o valor que deseja depositar: R$ "))
            saldo_conta = realizar_deposito(saldo_conta, quantia)
            consultar_saldo(saldo_conta)
        except ValueError:
            print("\nEntrada inválida! Digite um valor numérico.")

    elif opcao == '0':
        print("\nObrigado por utilizar o nosso Banco Digital!")
        break

    else:
        print("\nOpção inválida! Por favor, escolha um número entre 0 e 3.")