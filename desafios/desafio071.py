print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
num = float(input('Qual valor você quer sacar? R$ '))
total = num
ced = 100
ced_cont = 0
while True:
    if total >= ced:
        total -= ced
        ced_cont += 1
    else:
        if ced_cont > 0:
            print(f'Total de {ced_cont} cédulas de R${ced:.2f}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        ced_cont = 0
        if total == 0:
            break
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')

print()
valor = int(input('Quanto você quer sacar? R$ '))
lista1 = [valor // 50, (valor % 50)//20, ((valor % 50) % 20)//10, ((valor % 50) % 20) % 10]  # noqa
lista2 = ['R$50', 'R$20', 'R$10', 'R$1']
print(lista1)
for i in range(4):
    if (lista1[i] > 0):
        print(f'Total de {lista1[i]} cédulas de {lista2[i]}')

print()
valor = int(input('Digite o valor que será sacado: '))
lista = [50, 20, 10, 1]
c = 0
for elem in lista:
    while True:
        if elem <= valor:
            valor -= elem
            c += 1
        elif c > 0:
            print(f'{c} notas {elem}.')
            c = 0
            break
        else:
            break
