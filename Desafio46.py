#Crie um codigo que mostre na tela uma contagem regressiva para o estouro de fogos de artificio
#indo de 10 até 0
#com uma pausa de 1 segundo entre elas

import time
print('Contegem regressiva para estourar os fogos de artificio!')
for c in range(10, 0, -1):
    time.sleep(1)
    print(c)
print('KABUMMMMM')