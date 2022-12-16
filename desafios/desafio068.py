from random import randint
cont = soma = 0
print('-=-' * 8)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=-' * 8)
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    soma = computador + jogador
    par_impar = ' '
    while par_impar not in 'PI':
        par_impar = str(input('Par ou ímpar? [P/I] ')).upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} ', end='')  # noqa
    print('DEU PAR.' if soma % 2 == 0 else "DEU ÍMPAR.")
    if par_impar == 'P':
        if soma % 2 == 0:
            print('Você GANHOU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    elif par_impar == 'I':
        if soma % 2 == 1:
            print('Você GANHOU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {cont} vezes.')
