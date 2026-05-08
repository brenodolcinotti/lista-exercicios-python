nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade < 10:
    print(f"{nome}, vocêestá permitido a assistir a filmes apenas de conteúdo livre.")

elif 10 <= idade <= 13:
    print(f"{nome}, você está permitido a assistir a filmes apenas de classificação 10+.")

elif 14 <= idade <= 17:
    print(f"{nome}, você está permitido a assistir a filmes apenas de classificação 14+.")

else:
    print(f"{nome}, você está permitido a assistir a filmes apenas de classificação 18+.")