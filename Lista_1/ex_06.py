nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
situacao_academica = input("Digite sua situação acadêmica (Regular ou Irregular): ")

if idade < 12:
    print("Acesso negado, so é permitido a entrada com idade superior a 12 anos.")

elif idade >= 12 and idade <= 17 and situacao_academica == "Regular" or situacao_academica == "regular":
    print("Acesso autorizado, seja bem-vindo(a)", nome)

elif idade >= 12 and idade <= 17 and situacao_academica == "Irregular" or situacao_academica == "irregular":
    print("Acesso negado, sua situação acadêmica é irregular.")

elif idade >= 18:
    print("Acesso autorizado, seja bem-vindo(a)", nome)