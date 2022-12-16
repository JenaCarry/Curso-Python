def metade(preço=0, format=False):
    res = preço / 2
    return res if format is False else moeda(res)


def dobro(preço=0, format=False):
    res = preço * 2
    return res if format is False else moeda(res)


def aumentar(preço=0, taxa=0, format=False):
    res = preço + (preço * taxa / 100)
    return res if not format else moeda(res)


def diminuir(preço=0, taxa=0, format=False):
    res = preço - (preço * taxa / 100)
    return res if not format else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')


def resumo(preço=0, taxa_a=10, taxa_d=10):
    print('-' * 35)
    print('RESUMO DO VALOR'.center(35))
    print('-' * 35)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxa_a}% de aumento: \t{aumentar(preço, taxa_a, True)}')
    print(f'{taxa_d}% de aumento: \t{diminuir(preço, taxa_d, True)}')
    print('-' * 35)
