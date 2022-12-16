soma = cont = 0
while True:
    num = int(input('[999 para parar]\nDigite um número: '))
    if num == 999:
        break  # Para o looping
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi {soma}.')
