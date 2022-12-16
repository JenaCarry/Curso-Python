lar = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = alt * lar
tinta = area / 2  # Tinta rende 2mt²
print(f'Sua parede tem a dimensão de {lar}x{alt} e sua área é de {area}m²')
print(f'Para pintar essa parede, você precisará de {tinta}L de tinta')
