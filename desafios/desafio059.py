numeros = []
num = [int(input(f'{valor}º valor: ')) for valor in range(1, 3)]
numeros.append(num)
opçao = 0
while opçao != 5:
    print(f'''{'=-=' * 10}
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR NÚMERO
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opçao = int(input('>>> Qual é a sua opção? '))
    if opçao == 1:
        print(f'A soma entre {num[0]} e {num[1]} é {sum(num)}.')
    elif opçao == 2:
        print(f'O resultado de {num[0]} x {num[1]} é {num[0] * num[1]}.')
    elif opçao == 3:
        if num[0] == num[1]:
            print('Não exite número maior pois ambos são do mesmo valor.')
        else:
            print(f'Entre {num[0]} e {num[1]} o maior valor é {max(num)}.')
    elif opçao == 4:
        print('Informe os números novamente: ')
        num = [int(input(f'{valor}º valor: ')) for valor in range(1, 3)]
        numeros.append(num)
    if opçao == 0 or opçao > 5:
        print('Opção inválida! Tente novamente.')
print('Finalizando...')  # opção == 5
