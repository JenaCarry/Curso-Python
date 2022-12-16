# Variáveis compostas
# 2º Listas - Parte 2
teste = []  # type: list
teste.append('Lucas')
teste.append(26)
galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(f'{galera}\n')

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 43]]
print(galera[0])  # João 19 - Mostra tudo na posição 0
print(galera[0][0])  # João - Mostra apenas a posição 0
for pessoa in galera:
    # print(pessoa) - Mostra lista por lista
    # print(pessoa[0]) - Mostra apenas os nomes das listas
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')

galera2 = []  # type: list
dado = []  # type: list
maior = menor = 0
for cont in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera2.append(dado[:])
    dado.clear()

for pessoa in galera2:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior idade.')
        maior += 1
    else:
        print(f'{pessoa[0]} é menor de idade.')
        menor += 1
print(f'Temos {maior} maiores e {menor} menores de idade.')
