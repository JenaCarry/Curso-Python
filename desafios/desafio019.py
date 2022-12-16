from random import choice
alunos = [str(input(f'{valor}º aluno: ')).title() for valor in range(1, 5)]
print(f'O aluno escolhido foi o(a) {choice(alunos)}!')
