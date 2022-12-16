num = [float(input(f'{valor}º nota do aluno: ')) for valor in range(1, 3)]
print(f'A média entre {num[0]} e {num[1]} é igual a {sum(num) / len(num):.2f}.')  # noqa
