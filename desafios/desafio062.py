primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão Pa:'))
termo = primeiro
cont = tot = 0
more = 10
while more != 0:
    tot = more + tot
    while cont < tot:
        print(termo, end=' ')
        termo += razao
        cont += 1
    print('pausa')
    more = int(input('Quer ver mais quantos termos? '))
print(f'Progressão finalizada com {tot} termos mostrados.')
