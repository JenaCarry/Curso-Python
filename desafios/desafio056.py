idades = []
maior = cont_mulher = 0
homem_velho = ''
for c in range(1, 5):
    print(f'{f" {c}º pessoa ":-^20}')
    nome = str(input('nome: '))
    idade = int((input('Idade: ')))
    idades.append(idade)
    sexo = str(input('Sexo [M/F]: ')).upper()
    if sexo == 'M' and idade > maior:
        maior = idade
        homem_velho = nome
    if sexo == 'F' and idade < 20:
        cont_mulher += 1
print(f'A média de idade do grupo é de {sum(idades) / len(idades):.1f}.')
print(f'O homem mais velho tem {max(idades)} anos e se chama {homem_velho}.')
print(f'A todo temos {cont_mulher} mulheres com menos de 20 anos!')
