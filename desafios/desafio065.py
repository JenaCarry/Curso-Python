resp = 's'
soma = cont = media = 0.0
while resp == 's':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]: ')).strip().lower()[0]
    media = soma / cont
print(f'Você digitou {cont:.0f} números e a média foi de {media:.2f}.')
print(f'O maior número foi {maior} e o menor foi {menor}.')

resp = 's'
numeros = []  # type: list
while resp == 's':
    num = int(input('Digite um número: '))
    numeros.append(num)
    resp = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
print(f'Voce digitou {len(numeros)} números e a média foi de {sum(numeros) / len(numeros):.1f}')  # noqa
print(f'O maior número foi de {max(numeros)} e o menor foi de {min(numeros)}')
