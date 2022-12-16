from random import sample
from time import sleep
print('-'*30, '\n', '     JOGA NA MEGA SENA       \n', '-'*30)
games = []  # type: list
jogos = int(input('Quantos jogos quer que eu sorteie? '))
for i in range(0, jogos):
    games.append([])
print('-='*3, f' SORTEANDO {jogos} JOGOS ', '-='*3)
for i in range(0, jogos):
    games[i] = sample(range(60), 6)
    sleep(0.5)
    print(f'Jogo {i+1}: {games[i]}')
