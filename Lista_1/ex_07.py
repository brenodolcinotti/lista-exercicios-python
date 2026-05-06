nome_funcionario = input("Digite seu nome: ")
tarefas_concluidas = int(input("Digite o número de tarefas concluídas no mês: "))
erros_registrados = int(input("Digite o número de erros registrados nas tarefas: "))
faltas = int(input("Digite seu número de faltas no mês: "))

produtividade = "Produtividade Alta" if tarefas_concluidas >= 50 else "Produtividade Média" if tarefas_concluidas >= 30 and tarefas_concluidas< 50 else "Produtividade Baixa"

qualidade = "Qualidade Excelente" if erros_registrados <= 2 else "Qualidade Boa" if erros_registrados >= 3 and erros_registrados <= 5 else "Qualidade Ruim"

assiduidade = "Assiduidade Boa" if faltas <= 1 else "Assiduidade Regular" if faltas >= 2 and faltas <= 3 else "Assiduidade Ruim"

if produtividade == "Produtividade Alta" and qualidade == "Qualidade Excelente" or qualidade == "Qualidade Boa" and assiduidade == "Assiduidade Boa":
    print("Parabéns", nome_funcionario,"! Você é um Destaque.")

elif produtividade == "Produtividade Média" and qualidade == "Qualidade Boa" and assiduidade == "Assiduidade Regular":
    print(nome_funcionario,", você é um funcionario Adequado.")

else:
    print(nome_funcionario,", você é um funcionario Insatisfatório.")