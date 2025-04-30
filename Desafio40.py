#crie um codigo que calcule a media de 2 notas de um aluno
#Separe mensagens de acordo com a media dele
#media abaixo de 5.0: reprovado
#media entre 5.0 e 6.9: recuperação
#media 7.0 ou superior: aprovado
print()
print('Vamos calcular sua media para saber como está a sua situação')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2

print()
print('Sua media foi {:.2f}.'.format(media))
print()

if media >= 7.0:
    print('Parabéns, você está aprovado, continue assim!')
elif 5.0 <= media <= 6.9:
    print('Você está de recuperação, se esforce mais.')
elif media < 5.0:
    print('Você está reprovado, se esforce mais')
print()
