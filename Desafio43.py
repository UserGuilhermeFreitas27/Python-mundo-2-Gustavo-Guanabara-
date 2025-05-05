#desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status de acordo com a tabela
#Menor que 18,5 → Abaixo do peso
#18,5 a 24,9 → Peso normal
#25 a 29,9 → Sobrepeso
#30 a 34,9 → Obesidade grau 1
#35 a 39,9 → Obesidade grau 2
#40 ou mais → Obesidade grau 3 (obesidade mórbida)
print()
peso = float(input('digite seu peso: '))
altura = float(input('Digite sua altura: '))
print()
imc = peso / pow(altura, 2)

print('Seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso.') #não faz programação
elif 18.5 <= imc <= 24.9:
    print('Seu peso está normal.') #programa em html
elif 25.0 <= imc <= 29.9:
    print('Você está com sobrepeso.') #programador iniciante
elif 30.0 <= imc <= 34.9:
    print('Você está com obesidade grau 1.') #programador a 4 anos
elif 35.0 <= imc <= 39.9:
    print('Você está com obesidade grau 2.') # programador a 7 anos
else:
    print('Você está com obesidade grau 3 e sofre de obesidade mórbida') #programador premium plus s+ tipo A26 com problemas psicológicos
    print('Procure atendimento médico')
