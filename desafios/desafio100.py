from random import randint


def sorteia(lista):
    '''Sorteia e exibe 5 valores aleatórios.'''
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        num = randint(1, 10)
        lista.append(num)
        print(f'{num} ', end='')
    print('Pronto!')


def soma_par(lista):
    '''Mostra a soma dos pares na lista.'''
    soma_pares = 0
    for i in lista:
        if i % 2 == 0:
            soma_pares += i
    print(f'Somando os valores pares de {lista}, temos {soma_pares}.')


numeros = []  # type: list
sorteia(numeros)
soma_par(numeros)
