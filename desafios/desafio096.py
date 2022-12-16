def area(largura, comprimento):
    '''Calcula a área de um terreno.'''
    a = largura * comprimento
    print(f'A área de um terreno {largura:.1f}x{comprimento:.1f} é de {a:.1f}m².')  # noqa


# Programa principal
print('Controle de Terrenos'.center(40))
print('-' * 40)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)

# area(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (m): ')))
