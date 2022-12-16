viagem = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {viagem}km.')
preço = viagem * 0.50 if viagem <= 200 else viagem * 0.45
print(f'E o preço da sua passagem será de R${preço:.2f}.')
