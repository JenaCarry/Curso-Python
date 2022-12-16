# Funções - Parte 2
def fatorial(num=1):
    f = 1
    for valor in range(num, 0, -1):
        f *= valor
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')


def par(num=0):
    if num % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('É ímpar!')
# 1º Interactive help - Ajuda interativa
# help() - Retorna o que algo faz
# print(input.__doc__) - Retorna o que algo faz

# 2º Docstring
# help(contador) - Mostra o que a função faz

# 3º Argumentos opcionais
'''def somar(a=0, b=0, c=0):  # Valores padrão
    s = a + b + c
    print(f'A soma vale {s}')
somar(a=3, c=2, b=5)
somar(b=8, c=4)'''

# 4º Escopo de variáveis
'''def test(b):
    # global a - A dentro passa a ser A fora
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')
a = 5
test(a)
print(f'A fora vale {a}')'''
# Se a variável estiver na função ela é escopo local
# Se a variável estiver fora da função é escopo global

# 5º Retorno de resultados
'''def somar(a=0, b=0, c=0):  # Valores padrão
    s = a + b + c
    return s
print(somar(3, 2, 5))  # Posso por direto no print()
r1 = somar(3, 2, 5)  # Posso por numa variável
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus cálculos deram {r1}, {r2}, {r3}.')'''
