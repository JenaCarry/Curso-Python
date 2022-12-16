def leia_int(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')  # noqa
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return inteiro


def linha(tam=40):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(f'\033[1m{txt.center(40)}\033[m')
    # print(txt.center(40))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    for cont, item in enumerate(lista):
        print(f'\033[33m{cont + 1}\033[m - \033[34m{item}\033[m')
    print(linha())
    opc = leia_int('\033[32mSua opção: \033[m')
    return opc
