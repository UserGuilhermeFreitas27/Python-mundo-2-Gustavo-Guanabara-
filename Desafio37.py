#Crie um codigo que leia um numero inteiro qualquer
#Peça para o usuario escolher a base de conversão
#1 para binario
#2 para octal
#3 para hexadecimal
n = int(input('Digite um numero qualquer: '))
s = int(input('Escolha a base de conversão\n 1 Para Binario;\n 2 Para Octal;\n E 3 para Hexadecimal.'))

b = bin(n) #Binario
o = oct(n) #Octal
h = hex(n) #hexadecimal

if (s == 1):
    print('O numero {} convertido para Decimal é {}.'.format(n, b))
if (s == 2):
    print('O numero {} convertido para Octal é {}'.format(n, o))
if (s == 3):
    print('O numero {} convertido para Hexadecimal é {}'.format(n, h))
