#Crie um codigo que leia a idade de uma pessoa
#diga se ele vai ter que se apresentar ao exercito 
#Se é a hora de se apresentar
#Se já passou do tempo de alistamento
#Quanto tempo falta ou já passou do alistamento

idade = (int(input('Digite sua idade: ')))
idade0 = idade * 12

if idade < 18:
    print('Ainda não tem idade suficiente para servir, espere até completar 18 anos.')
    tempo1 = idade - 18 #O quanto ainda falta
    print('Ainda falta {} anos para você se alistar.'.format(abs(tempo1)))
elif idade == 18:
    print('Está na hora de se alistar, compareça ao exercito.')
elif idade > 18:
    print('Já passou da hora de se alistar\nSe apresente ao exercito o mais rapido possível!')
    tempo2 = idade - 18 #O quanto ja passou do tempo
    print('Seu alistamento já atrasou em {} anos'.format(tempo2))
