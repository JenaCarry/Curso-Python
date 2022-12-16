n = float(input('Qual o preço do produto? R$'))
novo = n - (n * 5 / 100)
print(f'O produto que custava R${n}, na promoção com desconto de 5% vai custar R${novo:.2f}')  # noqa
