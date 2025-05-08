#Crie um codigo que faça o computador jogar jokenpô com você
import random

print('Vamos jogar jokenpô')
escolhas = int(input('-1 Pedra.\n-2 Papel.\n-3 Tesoura.\n')) #escolha do jogador
lista = ['Pedra', 'Papel', 'Tesoura']

print()

if escolhas == 1:
    print('Você escolheu Pedra.')
elif escolhas == 2:
    print('Você escolheu Papel.')
else:
    print('Você escolheu Tesoura.')

com = random.choice(lista) #escolha do computador
print('O computador escolheu {}'.format(com))
escolhas = lista[escolhas - 1]

print()

if escolhas == com:
    print('Empate!')
elif (escolhas == 'Pedra' and com == 'Tesoura') or \
    (escolhas == 'Papel' and com == 'Pedra') or \
    (escolhas == 'Tesoura' and com == 'Papel'):
    print('Você venceu!')
else:
    print('Computador venceu!')
