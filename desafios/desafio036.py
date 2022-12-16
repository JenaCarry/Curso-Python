from colorful import gn, rd, nn
casa = float(input('Qual o valor da casa? R$ '))
salário = float(input('Qual é seu salário? R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * 0.3
if prestação <= mínimo:
    print(f'Para pagar uma casa de R${casa:.2f} reais em {anos} anos', end='')
    print(
        f' a prestação será de R${gn}{prestação:.2f}{nn} reais! {gn}\nEmpréstimo Concedido{nn}!')  # noqa
else:
    print(
        f'O valor da prestação é R${rd}{prestação:.2f}{nn} reais!\n{rd}Empréstimo Negado{nn}!')  # noqa
