# Variáveis compostas
# 3º Dicionários
dados = {'nome': 'Pedro', 'idade': 25}
dados['sexo'] = 'M'  # Adiciona um elemento ao dicionário
print(f'Me chamo {dados["nome"]} tenho {dados["idade"]}.\n')
del dados['sexo']  # Deleta o elemento sexo do dicionário

filme = {'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}
print(filme.values())  # Valores
print(filme.keys())  # Chaves
print(filme.items(), '\n')  # Chave-Valor

for k, v in filme.items():  # k = keys v = values
    print(f'O {k} é {v}')

locadora = [
    {'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'},
    {'titulo': 'Avengers', 'ano': 2012, 'diretor': 'Joss Whedon'},
    {'titulo': 'Matrix', 'ano': 1999, 'diretor': 'Wachowski'}
]
print(f'\n{locadora[0]["ano"]}\n')  # 0 lista - "ano" elemento


pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
pessoas['peso'] = 98.5
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
for k, v in pessoas.items():
    print(f'{k} = {v}', end='')
    print(', ' if v != pessoas['peso'] else '.', end='')

estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
estado3 = {'uf': 'São Paulo', 'sigla': 'SP'}
estados = [estado1, estado2]
print(f'\n{estados[0]["uf"]}\n')  # 0 lista - "uf" elemento

estado = {}  # type: dict
brasil1 = []  # type: list
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: ')).title()
    estado['sigla'] = str(input('Sigla do Estado: ')).upper()
    brasil1.append(estados.copy())  # Criar uma cópia
for e in brasil1:
    for v in e.values():
        print(v, end=' ')
    print()
