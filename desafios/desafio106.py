c = ('\033[m',  # 0 - sem cor
     '\033[41m',  # 1 - vermelho
     '\033[1;42m',  # 2 - verde
     '\033[1;46m',  # 3 - azul
     '\033[7m')  # 4 - invertido


def ajuda(com):
    print(c[4], end='')
    print(com.__doc__)
    print(c[0], end='')


def título(msg, cor=0):
    print(f'{c[cor]}~' * (len(msg) + 4))
    print(f'  {msg}')
    print('~' * (len(msg) + 4), end=f'{c[0]}\n')


# Programa principal
while True:
    título('SISTEMA DE PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando == 'fim':
        break
    else:
        título(f'Acessando o manual do comando \'{comando}\'', 3)
        ajuda(comando)
título('ATÉ LOGO!', 1)
