def fatorial(num, show=False):
    '''
    -> Calcula o fatorial de um número.
    :parâmetro num: O número a ser calculado.
    :parâmetro show: (opcional) Mostrar ou não a conta.
    :parâmetro return: O valor do Fatorial de um número (num).
    '''
    f = 1
    for valor in range(num, 0, -1):
        if show:
            print(f'{valor}', end=' x ' if valor > 1 else ' = ')
        f *= valor
    return f


# Programa principal
print('-' * 30)
print(fatorial(5, show=True))  # False ou True
# help(fatorial)
