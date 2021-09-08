
print("*************************************")
print("****Frutas!*****")
print("**************************************")

frutas = ['Banana', 'Maça', 'Pera', 'Uva', 'Melancia', 'Jamelão']
#print(frutas)
fruta_pedida = input('Qual é a fruta que deseja consultar ?')

if(fruta_pedida in frutas):
    print('Sim, temos a fruta.')
else:
    print('Não temos a fruta.')


