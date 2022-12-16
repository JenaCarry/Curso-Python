# ANSI == escape sequence
# \033[m  colocar cor no terminal
cores = {'none': '\033[m',  # Branco
         'grey': '\033[30m',  # Cinza
         'red': '\033[31m',  # Vermelho
         'green': '\033[32m',  # Verde
         'yellow': '\033[33m',  # Amarelo
         'purple': '\033[34m',  # Roxo
         'pink': '\033[35m',  # Rosa
         'cyan': '\033[36m',  # Ciano azul
         'preto-branco': '\033[7m'}  # Preto e Branco
a = 3
b = 5
nome = 'Jean'

print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m!')

print(f'Olá! Muito prazer em te conhecer, \033[4;34m{nome}\033[m!')

print(f'Olá! Muito prazer em te conhecer, {cores["cyan"]} \033[4m{nome} {cores["none"]}!')  # noqa

print('\033[0;37;41mOlá, Mundo!\033[m')
print('\033[4;33;44mOlá, Mundo!\033[m')
print('\033[1;35;43mOlá, Mundo!\033[m')
print('\033[30;42mOlá, Mundo!\033[m')
print('\033[mOlá, Mundo!\033[m')
print('\033[7;30mOlá, Mundo!\033[m')
print('\033[7mOlá, Mundo!\033[m')
