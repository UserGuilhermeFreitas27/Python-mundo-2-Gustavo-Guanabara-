#A confederação nacional de Natação precisa de um programa que
#leia o ano de nascimento de um atleta e mostre sua categoria
#de acordo com sua idade
#Até 9 anos: mirim
#até 14 anos: infatil
#Até 19 anos: Junior
#Até 20 anos: Sênior
#Acima: master
import datetime
print()
ano = int(input('Digite seu ano de nascimento: '))
idade = datetime.datetime.now().year - ano

if idade <= 9:
    print('Sua categoria é MIRIM, aproveite a disputa!')
elif 10 <= idade <= 14:
    print('Sua categoria é INFANTIL, aproveite a disputa!')
elif 15 <= idade <= 19:
    print('Sua categoria é JUNIOR, aproveite a disputa!')
elif idade == 20:
    print('Sua categoria é SENIOR, aproveite a disputa!')
else:
    print('Sua categoria é MASTER, aproveite a disputa!')
