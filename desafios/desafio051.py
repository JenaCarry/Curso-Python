primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
decimo = (primeiro + (10 - 1) * razao) + 1
for c in range(primeiro, decimo, razao):
    print(c, end=' → ')
print('Acabou')
