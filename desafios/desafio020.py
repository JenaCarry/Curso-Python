from random import shuffle
alunos = [str(input(f'{valor}º aluno: ')).title() for valor in range(1, 5)]
shuffle(alunos)
print('A ordem de apresentação será: ')
print(alunos)
