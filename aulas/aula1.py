from random import randint
from math import sqrt

nome = input('Qual é seu nome? ').title()
print(f'Prazer em te conhecer {nome:20}!')
print(f'Prazer em te conhecer {nome:>20}!')
print(f'Prazer em te conhecer {nome:<20}!')
print(f'Prazer em te conhecer{nome:^20}!')
print(f'Prazer em te conhecer {nome:=^20}!')

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'A soma é {s}, o produto é {m} e a divisão é {d:.2f}', end=', ')
print(f'divisão inteira {di} e potência {e}')

num = int(input('Digite um número: '))
print(f'A raiz  de {num} é igual a {sqrt(num):.2f}')

num = randint(1, 10)
print(num)
