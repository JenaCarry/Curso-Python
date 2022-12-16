sal = float(input('Qual é o salário do funcionário? R$'))
novo = sal + (sal * 15/100)
print(f'Seu salário é de R${sal} e com um aumento de 15%, passa a ser R${novo:.2f}')  # noqa
