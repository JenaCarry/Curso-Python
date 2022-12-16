numeros = []
while True:
    numeros.append(int(input('Digite um número: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Você digitou {len(numeros)} elementos.')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são {numeros}')
if 5 in numeros:
    print(f'O valor 5 faz parte da lista, e está na {numeros.index(5) + 1}º posição.')  # noqa
else:
    print('O valor 5 não foi encontrado na lista.')
