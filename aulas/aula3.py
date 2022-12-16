# Condições simples e compostas
tempo = int(input('Quantos anos tem seu carro? '))
print('Carro novo' if tempo <= 3 else 'Carro velho')  # condição simplificada
print('---FIM---')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'A sua média foi {m:.1f}')
print('Parabéns!' if m >= 6 else 'ESTUDE MAIS!')  # simplificado

nome = str(input('Qual é seu nome? ')).strip().title()
if nome == 'Jean':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal!')
print(f'Tenha um bom dia, {nome}!')
