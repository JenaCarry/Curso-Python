def leia_int(msg):
    while True:
        num = str(input(msg))
        if num.isnumeric():
            return int(num)
        else:
            print('\033[31mErro! Digite um número inteiro válido.\033[0m')


# Programa principal
num = leia_int('Digite um número: ')
print(f'Você acabou de digitar o número {num}')
