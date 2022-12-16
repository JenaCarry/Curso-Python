numeros = []  # type: list
while 999 not in numeros:
    num = int(input('[999 para parar]\nDigite um número: '))
    numeros.append(num)
numeros.pop()
print(f'Foram digitados {len(numeros)} números e a soma entre eles é {sum(numeros)}.')  # noqa

num = soma = cont = 0
num = int(input('[999 para parar]\nDigite um número: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('[999 para parar]\nDigite um número: '))
print(f'Foram digitados {cont} números e a soma entre eles é {soma}.')  # noqa
