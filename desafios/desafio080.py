lista = []  # type: list
for cont in range(0, 5):
    num = int(input('Digite um valor: '))
    if cont == 0 or num > lista[-1]:  # num >= max(lista)
        lista.append(num)
        print('Adicionando ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {lista}')

lista2 = []
reserva = [int(input('Digite um valor: ')) for c in range(0, 5)]
while len(reserva) != 0:
    lista2.append(min(reserva))  # lista2.append(max(reserva))
    reserva.remove(min(reserva))  # reserva.remove(max(reserva))
print(f'Os valores digitados em ordem foram {lista2}')
