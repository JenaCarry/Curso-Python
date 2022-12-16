from math import hypot
op = float(input('Comprimento do cateto oposto: '))
ad = float(input('Comprimento do cateto adjacente: '))
print(f'A hipotenusa vai medir {hypot(ad, op):.2f}')
