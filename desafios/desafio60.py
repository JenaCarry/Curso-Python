from math import factorial

# While
num = int(input('Calcular seu fatorial: '))
cont = num
fatorial = 1
print(f'Calculando {num}! = ', end='')
while cont > 0:
    print(cont, end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fatorial *= cont
    cont -= 1
print(fatorial)

# For
fact = 1
for valor in range(1, num + 1):
    fact *= valor
print(f'\nO fatorial de {num}! é {fact}.')
print(f'\nO fatorial de {num}! é {factorial(num)}.')

f = 1
n = num
print(f'\nCalculando {num}! = ', end='')
for valor in range(num, 0, -1):
    print(n, end='')
    print(' x ' if n > 1 else ' = ', end='')
    f *= valor
    n -= 1
print(f)
