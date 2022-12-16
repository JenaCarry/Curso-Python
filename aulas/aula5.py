n = int(input('Digite um número: '))
for valor in range(n):
    print(valor + 1, end=' ')
print('FIM')

i = int(input('Início: '))
f = int((input('Fim: ')))
p = int(input('Passo: '))
for c in range(i, f + 1, p):
    print(c, end=' ')
print('FIM')

num = [int(input(f'{valor}º número: ')) for valor in range(1, 4)]
print(f'O somatório de todos os valores foi {sum(num)}. \nFim')
