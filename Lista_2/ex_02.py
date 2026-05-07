def coletar_dados(quantidade_alunos):
    """Função para coletar nome e nota dos alunos"""
    notas = []
    nomes = []
    
    print(f"--- Registro de Notas dos Alunos ---")
    for i in range(quantidade_alunos):
        while True:
            try:
                nome = input(f"Digite o nome do {i+1}° aluno: ")
                nota = float(input(f"Digite a nota final de {nome}: "))
                
                nomes.append(nome)
                notas.append(nota)
                break
            except ValueError:
                print("Entrada inválida! Por favor, digite um número para a nota (ex: 8.5).\n")
                
    return notas

def calcular_media_turma(notas):
    return sum(notas) / len(notas)

def analisar_desempenho(notas, media):
    acima = 0
    abaixo = 0
    
    for nota in notas:
        if nota >= media:
            acima += 1
        else:
            abaixo += 1
            
    print("\n--- Análise de Desempenho da Turma ---")
    print(f"Média da turma: {media:.2f}")
    print(f"Alunos na média ou acima: {acima}")
    print(f"Alunos abaixo da média: {abaixo}")

notas_da_turma = coletar_dados(5) 
media_final = calcular_media_turma(notas_da_turma)
analisar_desempenho(notas_da_turma, media_final)