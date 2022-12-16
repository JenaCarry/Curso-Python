from colorful import yl, cy, gn, pk, nn
n = int(input('Digite um número para ver sua tabuada: '))
print(f'\tTabuada do {pk}{n}{nn}: ')
print('-' * 30)
for valor in range(1, 11):
    print(f'{yl}{n}{nn} X {cy}{valor:2}{nn} = {gn}{n * valor}{nn}')
print('-' * 30)
