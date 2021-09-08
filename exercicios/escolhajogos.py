import forca
import advinhacaofinal
def escolhe_jogo():
    print("*************************************")
    print("****Escolha seu jogo!***")
    print("**************************************")

    print('(1) Forca (2) Advinhação Final')
    jogo = int(input('Qual o jogo?'))

    if (jogo == 1):
        print('Jogando Forca')
        forca.jogar()
    elif (jogo == 2):
        print('Jogando Advinhação')
        advinhacaofinal.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()
