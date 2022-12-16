dados = []  # type: list
while True:
    dado = {}  # type: dict
    print('-' * 40)
    dado['Nome'] = str(input('Nome do dado: ')).title()
    partidas = int(input(f'Quantas partidas {dado["Nome"]} jogou? '))
    dado['Gols'] = [int(input(f'Quantos gols na partida {v + 1}? ')) for v in range(0, partidas)]  # noqa
    dado['Total'] = sum(dado['Gols'])
    dados.append(dado.copy())
    while True:
        continuar = str(input('\tQuer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if continuar == 'N':
        break

print('-' * 40)
print(f'{"Cod":<4}{"Nome":<15}{"Gols":<15}{"Total":<15}')
print('-' * 40)
for pos, valor in enumerate(dados):
    print(f'{pos:<4}', end='')
    for v in valor.values():
        print(f'{str(v):<15}', end='')
    print()

print('-' * 40)
while True:
    jogador = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if jogador == 999:
        break
    if jogador >= len(dados):
        print(f'ERRO! Não existe jogador com código {jogador}! Tente novamente.')  # noqa
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {dados[jogador]["Nome"]}:')
        for i, g in enumerate(dados[jogador]['Gols']):  # índice, gols
            print(f'   No jogo {i} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
