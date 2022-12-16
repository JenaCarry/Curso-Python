numeros = []
while True:
    numeros.append(int(input('Digite um número: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'A lista completa é {numeros}')
print(f'A lista de pares é {[n for n in numeros if n % 2 == 0]}')
print(f'A lista de ímpares é {[n for n in numeros if n % 2 == 1]}')

'''for numero in numeros:
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')'''
