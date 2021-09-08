print("*************************************")
print("Bem vindo ao jogo de advinhação!")
print("**************************************")

numero_secreto = 42
total_tentativas = 3

for rodada in range(1,total_tentativas + 1):
    print('Tentativas {} de {}' .format(rodada, total_tentativas))
    chute_str = input("Digite seu número entre 1 e 100:")
    print("Você", "digitou", chute_str)
    chute = int(chute_str)
    if(chute < 1 or chute > 100):
        print('Você deve digitar um número entre 1 e 100!')
        continue
    acertou = chute == numero_secreto
    maior = chute>numero_secreto
    menor = chute<numero_secreto

    if(acertou):
        print("Você acertou")
        break
    else:
        if(maior):
            print("Você errou, o seu chute foi maior que o número secreto")
        elif(menor):
            print("Você errou, o seu chute foi menor que o número secreto")


print("Game OVER")
