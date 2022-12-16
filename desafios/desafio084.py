lista_principal = []  # type: list
pesado = leve = 0
while True:
    lista_temp = []  # type: list
    lista_temp.append(str(input('Nome: ')).title())
    lista_temp.append(float(input('Peso: ')))
    lista_principal.append(lista_temp[:])
    pesado = lista_temp[1] if len(lista_principal) == 1 or lista_temp[1] > pesado else pesado  # noqa
    leve = lista_temp[1] if len(lista_principal) == 1 or lista_temp[1] < leve else leve  # noqa
    continuar = str(input('\tQuer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-' * 30, f'\nAo todo foram cadastradas {len(lista_principal)} pessoas.')
print(f'O mais pesado foi {pesado:.1f}kg, foram: ', end='')
for p in lista_principal:
    print(f'[{p[0]}] ' if p[1] == pesado else '', end='')
print(f'\nO mais leve foi {leve:.1f}kg, foram: ', end='')
for p in lista_principal:
    print(f'[{p[0]}] ' if p[1] == leve else '', end='')

'''
if len(lista_principal) == 1 or lista_temp[1] > pesado:
    pesado = pessoa[1]
if len(lista_principal) == 1 or lista_temp[1] < leve:
    leve = pessoa[1]
'''
