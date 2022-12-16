from colorful import yl, cy, nn
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print(f'O {yl}primeiro valor{nn} é {cy}maior{nn}!')
elif n2 > n1:
    print(f'O {yl}segundo valor{nn} é {cy}maior{nn}!')
else:
    print(f'{yl}Não exite{nn} valor maior, os dois são {cy}iguais{nn}!')
