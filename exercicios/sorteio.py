import random

print("*************************************")
print("O GRANDE SORTEIO!")
print("**************************************")

aluno1 = 'Paulo'
aluno2 = 'Juliana'
aluno3 = 'Tamires'

sorteado = random.randrange(0,4)
print('Sorteado')
if(sorteado == 1):
    print('Paulo')
elif(sorteado == 2):
    print('Juliana')
else:
    print('Tamires')
