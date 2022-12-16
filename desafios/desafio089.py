estudantes = []  # type: list
while True:
    estudantes.append([str(input('Nome: ').title()), float(input('1º nota: ')), float(input('2º nota: '))])  # noqa
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('\tQuer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-=-' * 8)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 24)
for p, v in enumerate(estudantes):
    print(f'{p:<4}{v[0]:<10}{sum(v[1:])/ 2:>7.1f}')
while True:
    print('-' * 24)
    aluno = int(input('Mostrar notas de qual aluno? [999] para sair: '))
    if aluno == 999:
        break
    if aluno <= len(estudantes) - 1:
        print(f'Notas de {estudantes[aluno][0]} são {estudantes[aluno][1:]}')
