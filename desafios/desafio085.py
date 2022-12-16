valores = [[], []]  # type: list
for v in range(1, 8):
    valor = int(input(f'Digite o {v}º valor: '))
    valores[0].append(valor) if valor % 2 == 0 else valores[1].append(valor)
print(f'Os valores pares digitados foram: {sorted(valores[0])}')
print(f'Os valores ímpares digitados foram: {sorted(valores[1])}')
