def contador(inicio, fim, passo):
    '''
    -> Exibe uma contagem na tela.
    :parâmetro inicio: início da contagem
    :parâmetro fim: fim da contagem
    :parâmetro passo: passo da contagem
    :parâmetro return: sem retorno
    '''
    print('-=-' * 12)
    passo = 1 if passo == 0 else passo
    print(f'Contando de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        for c in range(inicio, fim + 1, passo):
            print(f'{c} ', end='')
        print('FIM!')
    else:
        for c in range(inicio, fim - 1, -passo):  # passo * -1
            print(f'{c} ', end='')
        print('FIM!')


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=-' * 12)
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = abs(int(input('Passo: ')))  # abs() - valor absoluto
contador(inicio=i, fim=f, passo=p)
help(contador)
