dados = {}  # type: dict
dados['Nome'] = str(input('Nome do Jogador: ')).title()
partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
dados['Gols'] = [int(input(f'Quantos gols na partida {v}? ')) for v in range(0, partidas)]  # noqa
dados['Total'] = sum(dados['Gols'])
print('-=-' * 20)
print(dados)
print('-=-' * 20)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=-' * 20)
print(f'O jogador {dados["Nome"]} jogou {len(dados["Gols"])} partidas.')
for i, v in enumerate(dados['Gols']):
    print(f'\t=> Na partida {i}, fez {v} gols.')
print(f'Foi um total de {dados["Total"]} gols.')
