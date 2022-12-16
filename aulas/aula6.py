# Variáveis compostas
# 1º Tuplas - Tuplas são imutáveis
# Pode utilizar () ou não
lanches = ('hambúrguer', 'suco', 'pizza', 'pudim')
# lanches = 'hambúrguer', 'suco', 'pizza', 'pudim' - sem ()
print(lanches)  # Mostra a tupla
print(lanches[1])  # Suco
print(lanches[3])  # Pudim
print(lanches[-2])  # Pizza
print(lanches[1:3])  # Do 1 até o 2, sempre para uma casa antes
print(lanches[2:])  # Do 2 até o final
print(lanches[:2])  # Do 0 até 1, sempre para uma casa antes
print(f'{lanches[-2:]}\n')  # -2 até o final, Pizza, Pudim

print(f'{sorted(lanches)}\n')  # Deixa em ordem alfabética

for comida in lanches:
    print(f'Eu vou comer um {comida}.')
print('Acho que comi demais!\n')

for posição, comida in enumerate(lanches):
    # enumerate - Mostra a posição
    print(f'Eu vou comer um {comida} na posição {posição}.')
print('Acho que comi demais!\n')

for cont in range(0, len(lanches)):  # Mostra até a posição 3
    print(f'Eu vou comer um {lanches[cont]}.')
    # Mostra a posição
    # print(f'eu vou comer um {lanches[cont]} na posição {cont}.')
print('Acho que comi demais!\n')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)  # Concatena a tupla a + b
print(len(c))  # Mostra o comprimento da tupla
print(c.count(5))  # Mostra quantas vezes tem o "5" na tupla
print(c.index(8))  # Mostra a posição do "8"

pessoa = ('lucas', 22, 'm', 59.5)  # Aceita dados de tipos diferentes
print(f'\n{pessoa}')
del pessoa  # Exclui a tupla
