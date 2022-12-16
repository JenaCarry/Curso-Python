from colorful import pk, pr, rd, gn, cy, yl, nn
num = [float(input(f'{valor}º nota: ')) for valor in range(1, 3)]
m = sum(num) / 2
print(f'Tirando {pk}{num[0]}{nn} e {pr}{num[1]}{nn}, a média do aluno é {cy}{m:.1f}{nn}!')  # noqa
if m < 5.0:
    print(f'O aluno está {rd}REPROVADO{nn}!')
elif m > 5.0 and m < 7:  # 7 > m >= 5:
    print(f'O aluno está em {yl}RECUPERAÇÃO{nn}!')
else:
    print(f'O aluno está {gn}APROVADO{nn}!')
