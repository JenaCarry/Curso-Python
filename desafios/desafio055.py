pesos = [float(input(f'Peso da {c}º pessoa: ')) for c in range(1, 6)]
print(f'O maior peso foi de {max(pesos)}kg\n'
      f'O menor foi de {min(pesos)}kg!')
