#Elabore um programa que calcule o valor  a ser pago por um produto
#considerando seu preço normal e condição de pagamento
#a vista em dinheiro/cheque: 10% de desconto
#a vista no cartão: 5% de desconto
#2x no cartao: preço normal
#3x ou mais: 20% de juros

vp = float(input('Digite o valor do protudo: ')) #Valor do produto
fp = int(input('Escolha a forma de pagamento.\n -1 A vista Dinheiro/cheque.\n -2 A vista cartão.\n -3 2x no cartão.\n -4 3x ou mais no cartão.\n')) #Forma de pagamento
print()
if fp == 4:
    mes = int(input('Em quantos meses deseja pagar? '))
    parc_3x_ou_mais = vp * (1 + 0.20)**mes
print()

a_vista_din = vp * 0.9
a_vista_cartao = vp * 0.95
parc_2x = vp

print()

if fp == 1:
    print('Você ganhou um desconto de 10%!')
    print('O valor do seu produto será de R${:.2f}.'.format(a_vista_din))
elif fp == 2:
    print('Você ganhou um desconto de 5%!')
    print('O valor do seu produto será de R${:.2f}'.format(a_vista_cartao))
elif fp == 3:
    print('O valor total será {:.2f}'.format(parc_2x))
else:
    print('Se a compra for parcelada em 3x ou mais, terá juros de 20% ao mês')
    print('O valor do seu produto parcelado em {} meses, será de R${:.2f}.'.format(mes, parc_3x_ou_mais))
