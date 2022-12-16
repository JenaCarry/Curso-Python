cont_idade = cont_homem = cont_mulher = 0
while True:
    print('{:-^30}'.format(' Enquete '))
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        cont_idade += 1
    if sexo == 'M':
        cont_homem += 1
    if idade < 20 and sexo == 'F':
        cont_mulher += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('{:-^30}'.format(' Resultado da Enquete '))
print(f'Total de pessoas com mais de 18 anos: {cont_idade}')
print(f'Ao todo temos {cont_homem} homens cadastrados.')
print(f'E temos {cont_mulher} mulheres com menos de 20 anos.')
