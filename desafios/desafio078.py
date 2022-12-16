numeros = [int(input(f'Digite um número para a posição {c + 1}: ')) for c in range(0, 5)]  # noqa
print(f'Você digitou os números {numeros}')
print(f'O maior valor digitado foi {max(numeros)} nas posições ', end='')
for pos, num in enumerate(numeros):
    if max(numeros) == num:
        print(f'{pos + 1}...', end='')
print(f'\nO menor valor digitado foi {min(numeros)} nas posições ', end='')
for pos, num in enumerate(numeros):
    if min(numeros) == num:
        print(f'{pos + 1}...', end='')

'''
if cont == 0:
    mai = men = numeros[cont]
else:
    if numeros[cont] > mai:
        mai = numeros[cont]
    if numeros[cont] < men:
        men = numeros[cont]
'''
