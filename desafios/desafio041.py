from colorful import yl, gn, cy, pr, pk, nn
from datetime import date
nasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print(f'O atleta tem {idade} anos')
if idade <= 9:
    print(f'Classificação: {yl}MIRIM{nn}.')
elif idade <= 14:
    print(f'Classificação: {gn}INFANTIL{nn}.')
elif idade <= 19:
    print(f'Classificação: {cy}JUNIOR{nn}.')
elif idade <= 25:
    print(f'Classificação: {pr}SÊNIOR{nn}.')
else:
    print(f'Classificação: {pk}MASTER{nn}.')
