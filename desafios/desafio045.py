from time import sleep
from random import randint
from colorful import pk, cy, yl, gn, rd, nn
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('{:=^40}'.format(f'{pk} Jogo de Jokenpô {nn}'))
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print(f'{cy}JO{nn}')
sleep(0.5)
print('{:^18}'.format(f'{yl}KEN{nn}'))
sleep(0.5)
print('{:^28}'.format(f'{gn}PÔ{nn}!'))
if jogador <= 2:
    print('-=' * 12)
    print(f'Computador jogou {(itens[computador])}')
    print(f'Jogador jogou {(itens[jogador])}')
    print('-=' * 12)
if computador == jogador:  # Empate
    print(f'{yl}EMPATE{nn}!')
elif (computador == 0 and jogador == 2) or (computador == 1 and jogador == 0) or (computador == 2 and jogador == 1):  # noqa
    print(f'{rd}PERDEU{nn}!')
elif (jogador == 0 and computador == 2) or (jogador == 1 and computador == 0) or (jogador == 2 and computador == 1):  # noqa
    print(f'{gn}GANHOU{nn}!')
else:
    print(f'{rd}JOGADA INVÁLIDA{nn}!')
