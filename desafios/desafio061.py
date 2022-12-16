primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 0
while cont < 10:
    print(termo, end=' → ')
    termo += razao
    cont += 1
print('FIM!')
