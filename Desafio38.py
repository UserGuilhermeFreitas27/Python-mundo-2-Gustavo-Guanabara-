#Crie um codigo que leia dois numeros
#Diga se o primeiro numero é o maior ou não
#Diga se o segundo numero é o maior ou não
#Ou se não existe um numero maior

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n1 > n2:
    print('O numero {} é o maior numero.'.format(n1))
if n2 > n1:
    print('O numero {} é o maior numero.'.format(n2))
if n1 == n2:
    print('Não existe numero maior, os dois são iguais.')
