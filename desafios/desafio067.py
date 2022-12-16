while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    print('-' * 40)
    if num < 0:
        break
    for valor in range(1, 11):
        print(f'{num} X {valor:2} = {num * valor}')
    print('-' * 40)
print('Programa tabuada encerrado. Volte sempre!')
