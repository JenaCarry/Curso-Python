from operator import itemgetter
from random import randint
valores = {}  # type: dict
cont = 1
print('Valores Sorteados: ')
for j in range(1, 5):
    valores[f'Jogador {j}'] = randint(1, 6)
for k, v in valores.items():
    print(f'\tO {k} tirou {v}')

# ordenado = {k: v for k, v in sorted(valores.items(), key=lambda item: item[1], reverse=True)}  # noqa
print('\nRanking dos Jogadores: ')
# ordena o dicionário com base no conjunto de valores
for k, v in sorted(valores.items(), key=itemgetter(1), reverse=True):
    print(f'\t{cont}º lugar: {k} com {v}')
    cont += 1
print()

# ordena o dicionário sem importar módulo
rank = sorted(valores.items(), key=lambda x: x[1], reverse=True)
print('\nRanking dos Jogadores: ')
for p, v in enumerate(rank):
    print(f'\t{p + 1}º lugar: {v[0]} com {v[1]}')
# lambda função anônima
# lambda parâmetro: parâmetro * 3 - vai retornar o valor * 3
