from time import sleep
num = int(input('Digite um número: '))
print('1 - Binário \n2 - Octal \n3 - Hexadecimal')
convert = int(input('Escolha uma das base de conversão acima: '))
print('CONVERTENDO...')
sleep(1)
if convert == 1:
    print(f'O número {num} convertido para Binário é {format(num, "b")}.')
elif convert == 2:
    print(f'O número {num} convertido para Octal é {format(num, "o")}.')
elif convert == 3:
    print(f'O número {num} convertido para Hexadecimal é {format(num, "x")}.')
else:
    print('Opção inválida! Tente novamente.')
