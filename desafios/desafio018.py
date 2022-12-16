import math
num = float(input('Informe um ângulo: '))
sen = math.sin(math.radians(num))
cos = math.cos(math.radians(num))
tg = math.tan(math.radians(num))
print(f'O ângulo de {num} tem o seno de {sen:.2f}')
print(f'O ângulo de {num} tem o cosseno de {num} é {cos:.2f}')
print(f'O ângulo de {num} tem a tangente de {num} é {tg:.2f}')
