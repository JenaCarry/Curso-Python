from datetime import datetime
atual = datetime.now().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')
if idade < 18:
    print(f'Ainda falta {18 - idade} anos para o alistamento.')
    print(f'Seu alistamento será em {(18 - idade) + atual}.')
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade > 18:
    print(f'Você já deveria ter se alistado há {idade - 18} anos.')
    print(f'Seu alistamento foi em {atual - (idade - 18)}.')
