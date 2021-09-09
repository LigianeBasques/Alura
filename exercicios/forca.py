def jogar ():

    print("*************************************")
    print("Bem vindo ao jogo de FORCA!")
    print("**************************************")

    palavra_secreta = 'banana'
    letras_acertadas = ["_", "_","_","_","_","_"]

    enforcou = False
    acertou = False
    erros = 0


    print(letras_acertadas)

    #enquanto não enforcou e não acertou
    while(not enforcou and not acertou):
        chute = input('Qual a letra?')
        chute = chute.strip()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() ==  letra.upper()):
                    letras_acertadas[index] = letra

                index = index + 1
        else:
            erros = erros + 1

        print(letras_acertadas)

    print("Game OVER")

if(__name__ == "__main__"):
    jogar()
