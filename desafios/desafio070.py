soma = cont = cont_mil = menor = 0
barato = ''
print('-' * 40)
print('\tLOJA DO JENA')
print('-' * 40)
while True:
    nome = str(input('Nome do Produto: '))
    preco = int(input('Preço: R$ '))
    cont += 1
    soma += preco
    if preco >= 1000:
        cont_mil += 1
    if cont == 1 or preco < menor:  # maneira simplificada
        menor = preco
        barato = nome
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {cont_mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
print()

produtos = []  # type: list
precos = []  # type: list
while True:
    produto = str(input('Nome do produto: '))
    preco = int(input('Preço: R$ '))
    produtos.append(produto)
    precos.append(preco)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${sum(precos):.2f}')
print(f'Temos {len([i for i in precos if i > 1000])} produto(s) custando mais que R$1.000,00')  # noqa
print(f'O produto mais barato foi {produtos[precos.index(min(precos))]} e custou R${min(precos)}')  # noqa
