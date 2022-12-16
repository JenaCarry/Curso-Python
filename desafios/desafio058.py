from random import randint
tentativas = 1
computador = randint(0, 10)  # Faz o computador "PENSAR"
print('Acabei de pensar em número entre 0 e 10.')
print('Será que você consegue adivinhar?')
jogador = int(input('Qual é seu palpite? '))  # Jogador tenta adivinhar
while jogador != computador:
    if jogador < computador:
        print('Mais... Tente mais uma vez.')
    else:
        print('Menos... Tente mais uma vez.')
    jogador = int(input('Qual é seu palpite? '))  # Jogador tenta adivinhar
    tentativas += 1
print(f'Acertou com {tentativas} tentativas. Parabéns!')
