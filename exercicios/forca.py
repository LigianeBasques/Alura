def jogar ():

    print("*************************************")
    print("Bem vindo ao jogo de FORCA!")
    print("**************************************")

    palavra_secreta = 'banana'
    enforcou = False
    acertou = False

    #enquanto não enforcou e não acertou
    while(not enforcou and not acertou):
        chute = input('Qual a letra?')
        chute = chute.strip()
        index = 0
        for letra in palavra_secreta:
            if(chute.upper() ==  letra.upper()):
                print('Encontrei a letra {} na posição {}'.format(letra,index))
            index = index + 1

        print('Jogando...')

    print("Game OVER")

if(__name__ == "__main__"):
    jogar()
