def maior(*num):
    '''Exibe o maior número.'''
    print('-=-' * 16)
    mai = 0
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        if valor > mai:
            mai = valor
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {mai}.')


# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
