from datetime import datetime
dados = {}  # type: dict
dados['Nome'] = str(input('Nome: ')).title()
dados['Idade'] = datetime.now().year - int(input('Ano de nascimento: '))
dados['CTPS'] = int(input('Carteira de Trabalho ("0" se não tiver): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$ '))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Contratação'] + 35) - datetime.now().year)  # noqa
print('-=-' * 16)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')
