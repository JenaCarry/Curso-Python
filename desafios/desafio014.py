# Celsius f = c x 1,8 + 32 ou ((9 * c) / 5) + 32
# Fahrenheit c = (F - 32) / 1,8
c = float(input('Informe a temperatura em °C: '))
fc = ((9 * c) / 5) + 32
print(f'A temperatura de {c}°C corresponde a {fc}°F!')

f = float(input('Informe a temperatura em °F: '))
cf = (f - 32) / 1.8
print(f'A temperatura de {f}°F corresponde a {cf}°C')
