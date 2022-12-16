enquetes = []  # type: list
soma = media = 0.0
while True:
    pessoa = {}  # type: dict
    pessoa['Nome'] = str(input('Nome: ')).title()
    while True:
        pessoa['Sexo'] = str(input('Sexo: [M/F] ')).title()
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    enquetes.append(pessoa.copy())
    while True:
        continuar = str(input('Quer continuar? ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if continuar == 'N':
        break
print('-=-' * 16)
print(f'- Ao todo temos {len(enquetes)} pessoas cadastradas.')
media = soma / len(enquetes)
print(f'- A média de idade é {media:5.2f} anos.')
print('- As mulheres cadastradas foram: ', end='')
for p in enquetes:
    if p['Sexo'] in 'F':  # if p['Sexo'] == 'F':
        print(p['Nome'], end=', ' if p != enquetes[-1] else '.')
print('\n- Listas de pessoas que estão acima da média: \n')
for p in enquetes:
    if p['Idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v}', end='; ' if k != 'Idade' else '.\n')
        print()
print('<< ENCERRANDO >>')
