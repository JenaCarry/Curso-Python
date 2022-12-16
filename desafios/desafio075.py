numeros = tuple(int(input(f'{valor}º número: ')) for valor in range(1, 5))
print(numeros)
print(f'O valor 9 apareceu {numeros.count(9)} vezes.')
print(f'O valor 3 apareceu na {numeros.index(3) + 1}º posição.' if 3 in numeros else 'Não há o número 3')  # noqa
print('Os valores pares digitados foram ', end='')
for numero in numeros:
    if numero % 2 == 0:
        print(numero, end=' ')
print(f'\nO valores ímpares digitados foram {[c for c in numeros if c % 2 == 1 or c == 1]}')  # noqa
