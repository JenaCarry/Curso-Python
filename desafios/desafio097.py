def escreva(txt):
    '''Exibe uma mensagem personalizada.'''
    tam = len(txt) + 4
    print('~' * tam)
    print(f'{txt:^{tam}}')  # center(len(txt) + 4)
    print('~' * tam)


# Programa principal
escreva(str(input('Escreva uma mensagem: ')).title())
