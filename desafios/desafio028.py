from random import randint
from time import sleep  # Faz o computador esperar
pc = randint(0, 5)  # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))  # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(1)  # Quantos segundos para esperar
print(pc)
if jogador == pc:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'Ganhei! Eu pensei no número {pc} e não no {jogador}!')
