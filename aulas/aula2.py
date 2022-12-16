frase = 'Curso em Video Python'
# Fatiamento
print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])
print('{:^40}'.format(frase))

# Análise
print(len(frase))  # comprimento da frase
print(frase.count('o'))  # conta a quantidade de algo
# conta a quantidade de algo a partir de 0 até 13
print(frase.count('o', 0, 13))
print(frase.find('deo'))  # encontra algo
print(frase.find('Curso'))  # retorna valor -1 caso não exista
print('Curso' in frase)  # encontra algo e retorna valor True ou False

# Transformação
print(frase.replace('Python', 'Android'))  # substitui um pelo outro
print(frase.upper())  # deixa as letras em maiúsculas
print(frase.lower())  # deixa as letras em minúsculas
print(frase.capitalize())  # deixa somente a 1° letra em maiúscula
print(frase.title())  # deixa todas as iniciais em maiúsculas
frase2 = '   Aprenda Python   '
print(frase2.strip())  # remove os espaços inúteis do início e do final
print(frase2.rstrip())  # remove os espaços inúteis da direita (right)
print(frase2.lstrip())  # remove os espaços inúteis da esquerda (left)

# Divisão
print(frase.split())  # divide a frase

# Junção
print('-'.join(frase.split()))
