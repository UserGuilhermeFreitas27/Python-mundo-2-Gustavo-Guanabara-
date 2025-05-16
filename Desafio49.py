#Refaça o exercicio 9, mostrando a tabuada do numero que o usuario escolher
#usando o laço "FOR"

c = int(input('Digite o numero que deseja saber a tabuada: '))
for i in range(1, 11):
    print('{} x {} = {}'.format(c, i, c * i))
