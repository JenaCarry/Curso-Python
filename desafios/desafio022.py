nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é', nome.upper())
print('Seu nome em minúsculas é', nome.lower())
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")}')
letra = nome.split()
print(f'Seu primeiro nome é {letra[0]} e ele tem {len(letra[0])} letras')