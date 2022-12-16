from colorful import rd, gn, nn
n = int(input('Digite um número: '))
d = n * 2  # Dobro
t = n * 3  # Triplo
r = n ** (1/2)  # Raiz quadrada
print(f'O dobro de {rd}{n}{nn} vale {gn}{d}{nn}.')
print(f'O triplo de {rd}{n}{nn} vale {gn}{t}{nn}.')
print(f'A raiz quadrada de {rd}{n}{nn} vale {gn}{r:.2f}{nn}.')
