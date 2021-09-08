import random

def jogar ():

    print("*************************************")
    print("Bem vindo ao jogo de advinhação!")
    print("**************************************")

    numero_secreto = random.randrange(1,101)
    total_tentativas = 0
    pontos = 1000

    print('Qual o nível de dificuldade?')
    print('(1) Fácil (2) Médio (3) Dificíl')

    nivel = int(input('Defina o nível: '))

    if (nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5



    for rodada in range(1,total_tentativas + 1):
        print('Tentativas {} de {}' .format(rodada, total_tentativas))
        chute_str = input("Digite seu número entre 1 e 100:")
        print("Você", "digitou", chute_str)
        chute = int(chute_str)
        if(chute < 1 or chute > 100):
            print('Você deve digitar um número entre 1 e 100!')
            continue
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou, o seu chute foi maior que o número secreto")
            elif(menor):
                print("Você errou, o seu chute foi menor que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Game OVER")

if(__name__ == "__main__"):
    jogar()
