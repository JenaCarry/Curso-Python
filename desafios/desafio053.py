frase = input('Digite uma palavra ou frase: ').strip().upper().replace(' ', '')
inverso = frase[::-1]
print(f'O inverso de {frase} é {inverso}')
if frase == inverso:
    print('A frase digitada é um Palíndromo!')
else:
    print('A frase digitada não é um Palíndromo!')
