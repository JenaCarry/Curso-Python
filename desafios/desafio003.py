from colorful import rd, pr, gn, nn
num = [int(input(f'{valor}º número: ')) for valor in range(1, 3)]
print(f'A soma entre {rd}{num[0]}{nn} e {pr}{num[1]}{nn} é {gn}{sum(num)}{nn}.')  # noqa
