num = int(input('Quantos termos você quer mostrar: '))
anterior = cont = soma = 0
proximo = 1
while cont < num:
    print(anterior, end=' → ')
    soma = anterior + proximo
    anterior = proximo
    proximo = soma
    cont += 1
print('FIM')

a, b = 0, 1
cont = 0
while cont < num:
    print(a, end=' → ')
    a, b = b, a + b
    cont += 1
print('FIM')
