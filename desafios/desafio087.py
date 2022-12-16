matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # type: list
par = coluna3 = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))  # noqa
        par += matriz[linha][coluna] if matriz[linha][coluna] % 2 == 0 else 0
        coluna3 += matriz[linha][coluna] if coluna == 2 else 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'{matriz[linha][coluna]:^5}', end='')
    print()
print(f'\nA soma dos valores pares é {par}.')
print(f'A soma dos valores da 3º coluna é {coluna3}.')
print(f'O maior valor da 2º linha é {max(matriz[1])}.')
