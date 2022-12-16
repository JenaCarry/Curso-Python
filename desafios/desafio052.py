from colorful import cy, yl, nn
cont = tot = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1):
    if num % c == 0:
        cont += 1
        tot += 1
        print(f'{cy}', end='')  # Azul é primo
    else:
        print(f'{yl}', end='')  # Amarelo não é primo
    print(f'{c}', end=f' {nn} ')
print(f'\nO número {num} foi divisível {tot} vezes.')
if cont == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele é NÃO É PRIMO!')
