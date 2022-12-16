tabela = (
    'Palmeiras',
    'Internacional',
    'Fluminense',
    'Corinthians',
    'Flamengo',
    'Athletico-PR',
    'Atlético-MG',
    'Fortaleza',
    'São Paulo',
    'América-MG',
    'Botafogo',
    'Santos',
    'Goiás',
    'Bragantino',
    'Coritiba',
    'Cuiabá',
    'Ceará SC',
    'Atlético-GO',
    'Avaí',
    'Juventude',
    'Chapecoense',
)
print('Os 5 primeiros colocados são: ')
# print(tabela[:5])
for time in tabela[:5]:
    print(f'\t{time}')
print('\nOs 4 últimos colocados são: ')
# print(tabela[-4:])
for time in tabela[-4:]:
    print(f'\t{time}')
print(sorted(tabela))
print(f'O Chapecoense está na {tabela.index("Chapecoense") + 1}º posição.')
