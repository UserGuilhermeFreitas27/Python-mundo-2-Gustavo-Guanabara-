#Crie um Codigo que leia 3 retas
#e faça com que esse codigo diga se essas 3 retas podem formar um triangulo ou não
#Mostre que tipo de triangulo pode ser formado com as retas
r1 = float(input('Digite o comprimento da reta1: '))
r2 = float(input('Digite o comprimento da reta2: '))
r3 = float(input('Digite o comprimento da reta3: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print("As retas podem formar um triângulo.")
    
    #Tipos de triangulo
    if r1 == r2 == r3:
        print("Triângulo: Equilátero, todos os lados iguais.")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("Triângulo: Isósceles, tem dois lados iguais.")
    else:
        print("Triângulo: Escaleno, tem todos os lados diferentes.")
else:
    print("As retas não formam um triângulo.")
