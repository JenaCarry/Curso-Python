# Preço normal em até 2x no Cartão
preço = float(input('Preço das compras: R$'))
print('''Formas de pagamento:
[ 1 ] à vista no Dinheiro / Cheque
[ 2 ] à vista do Cartão
[ 3 ] 2x no Cartão
[ 4 ] 3x ou mais no Cartão''')  # Forma de pagamento
opçao = int(input('Qual é a opção de pagamento? '))
if opçao == 1:
    # Desconto de 10% à vista no Dinheiro/Cheque
    print(f'Sua compra de R${preço} vai custar R${preço - (preço * 0.1):.2f}.')
elif opçao == 2:
    # Desconto de 5% à vista Cartão
    print(
        f'Sua compra de R${preço} vai custar R${preço - (preço * 0.05):.2f}.')
elif opçao <= 3:
    print(f'Sua compra será parcelada em 2x de R${preço / 2:.2f} SEM JUROS!')
    print(f'Sua compra de R${preço} vai custar R${preço}.')
elif opçao == 4:
    parcela = int(input('Em quantas vezes gostaria de parcelar a compra: '))
    # Juros de 20% em 3x ou mais no Cartão
    print(f'Sua compra será parcelada em {parcela}x de R${preço / parcela:.2f} COM JUROS!')  # noqa
    print(f'Sua compra de R${preço} vai custar R${preço + (preço * 0.2)}.')
