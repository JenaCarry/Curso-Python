# Funções - Parte 1
def linha():
    '''Mostra uma linha.'''
    print('-' * 20)


def titulo(txt):
    '''Recebe um parâmetro com linhas acima e abaixo.'''
    print('-' * 20)
    print(txt)
    print('-' * 20)


def soma(a, b):
    '''Soma A + b.'''
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


def contador(*num):
    '''Recebe vários valores em tupla.'''
    tamanho = len(num)
    # for valor in num:
    #     print(f'{valor} ', end='')
    print(f'Recebi os valores {num} e são ao todo {tamanho} números.')


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


titulo('  Curso em Vídeo   ')

soma(4, 9)
# soma(a=4, b=5)

contador(2, 7, 9)
contador(9, 0, 1, 6)

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
