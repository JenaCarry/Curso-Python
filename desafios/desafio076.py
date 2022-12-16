print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
lista_compras = (
    'Lápis', 1.75,
    'Borracha', 2,
    'Caderno', 15.9,
    'Estojo', 25,
    'Transferidor', 4.2,
    'Compasso', 9.99,
    'Mochila', 120.32,
    'Caneta', 22.3,
    'Livro', 34.9,
)
for posição in range(0, len(lista_compras), 2):
    print(f'{lista_compras[posição]:.<30}',
          f'R${lista_compras[posição + 1]:>7.2f}')
print()

for posição2 in lista_compras[::2]:
    print(f'{posição2:.<30}',
          f'R${lista_compras[lista_compras.index(posição2) + 1]:>7.2f}')
print()

for posição3 in lista_compras:
    if type(posição3) is str:
        print(f'{posição3:.<30}', end='')
    else:
        print(f'R$ {posição3:>7.2f}')
print()

for posição in range(0, len(lista_compras)):
    if posição % 2 == 0:
        print(f'{lista_compras[posição]:.<30}', end='')
    else:
        print(f'R${lista_compras[posição]:>7.2f}')
