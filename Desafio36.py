#Crie um codigo que aprove um emprestimo bancário para a compra de uma casa.
#O programa deve perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar
#calcule o valor da prestação mensal, sendo que não pode ser maior que 30% do salario, se não sera invalido o emprestimo

c = float(input('Digite o valor da casa: '))
s = float(input('Digite seu salario: '))
a = float(input('Em quantos anos pretende pagar? '))

mensal = a * 12 #Ano p/ mes
prestacao = c / mensal #Valor da casa dividido nas prestações

if prestacao<=(s*0.30):
    print('')
    print('Seu emprestimo foi aprovado!')
    print('Sua prestação é de R${:.2f}.'.format(prestacao))
else:
    print('')
    print('Seu imprestimo não foi aprovado.')
    print('')
    print('Sua prestação foi de R${:.2f}'.format(prestacao))
