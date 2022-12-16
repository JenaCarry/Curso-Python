from random import sample
from random import randint
numeros = (
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
)
print('Os valores sorteados foram: ', end='')
for numero in numeros:
    print(numero, end=' ')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')

# sample(sequence, k)
# sequence - Pode ser qualquer sequência: list, set, range, etc.
# k - O tamanho da lista retornada
# tuple() para fazer/criar uma tupla
valores = tuple(sample(range(10), 5))
print(valores)
print(f'O maior valor sorteado foi {max(valores)}')
print(f'O menor valor sorteado foi {min(valores)}')
