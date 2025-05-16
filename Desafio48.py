#Crie um codigo que calcule a some de todos os numeros impares
#que são multiplos de 3
#de 1 até 500

cont = 1
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print('soma {}'.format(soma))
print('Quantidade de numeros {}'.format(cont))
