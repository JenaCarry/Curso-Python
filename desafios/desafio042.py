from colorful import cy, rd, nn
print('-=-' * 8)
print('Analisador de Triângulos')
print('-=-' * 8)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Os segmentos {r1}, {r2} e {r3} PODEM FORMAR um triângulo ', end='')
    if r1 == r2 == r3:
        print(f'{cy}Equilátero!{nn}.')
    elif r1 != r2 != r3 != r1:
        print(f'{cy}Escaleno!{nn}.')
    else:
        print(f'{cy}Isósceles!{nn}.')
else:
    print(f'Os segmentos {r1}, {r2} e {r3} NÂO PODEM FORMAR um {rd}Triângulo{nn}.')  # noqa
