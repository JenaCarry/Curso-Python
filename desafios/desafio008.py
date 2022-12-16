from colorful import gn, gy, yl, pr, rd, pk, nn
n = float(input('Uma distância em metros: '))
km = n / 1000
hm = n / 100
dam = n / 10
dm = n * 10
cm = n * 100
mm = n * 1000
print(f'A medida de {gn}{n}{nn}m corresponde a: ')
print(f'{gy}{km}{nn}km \n{rd}{hm}{nn}hm \n{gn}{dam}{nn}.')
print(f'{yl}{dm}{nn}dm \n{pr}{cm}{nn}cm \n{pk}{mm}{nn}mm.')
