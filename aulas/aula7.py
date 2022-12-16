# Variáveis compostas
# 2º Listas - Parte 1
numeros = [2, 5, 9, 1]
numeros[2] = 3  # Muda o 9 para 3
numeros.append(7)  # Adiciona o 7 no final da lista
numeros.insert(2, 2)  # Adiciona 2 na posição 2
numeros.pop()  # Remove o último elemento ou valor desejado
numeros.remove(2)  # Remove o 2 primeira aparição
print(numeros)
numeros.sort()  # Deixa em ordem permanente
print(f'\nOrdem permanente {numeros}')
numeros.sort(reverse=True)  # Deixa em ordem inversa permanente
print(f'Ordem inversa permanente {numeros}')
print(f'\nOrdem {sorted(numeros)}')  # Deixa em ordem
print(f'Ordem inversa {sorted(numeros, reverse=True)}')  # Deixa em ordem
print(f'\nEssa lista tem {len(numeros)} elementos.')

valores = []  # type: list
# valores = list() - Outra maneira de criar lista
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)
for valor in valores:
    print(f'{valor}', end=' ')
print('\n')
for chave, valor in enumerate(valores):
    print(f'Na posição {chave} encontrei o valor {valor}!')
print('\n')

valores2 = []  # type: list
for cont in range(1, 3):
    valores2.append(int(input(f'{cont}º número: ')))
print(f'{valores2}\n')
# Outra maneira fora do "for"
valores3 = [int(input(f'{valor}º número: ')) for valor in range(1, 3)]
print(f'{valores3}\n')

idades = [2, 4, 23, 8]
cont = 0
for idade in idades:
    if idade < 20:
        cont += 1
print(cont)
print(f'{[idade for idade in idades if idade < 20]}')
# Mostra o comprimento
print(f'{len([idade for idade in idades if idade < 20])}\n')

a = [2, 3, 4, 7]
b = a[:]  # Faz uma cópia da lista A
b[2] = 8  # Muda o 4 para 8
print(f'Lista A: {a}')
print(f'Lista A: {b}')
