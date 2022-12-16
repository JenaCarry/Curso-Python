from colorful import gn, nn
real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 3.27  # U$1,00 = R$3,27
print(f'Com R${gn}{real}{nn} você pode comprar U${gn}{dolar:.2f}{nn}')
