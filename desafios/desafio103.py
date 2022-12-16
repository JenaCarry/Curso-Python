def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


nome = str(input('Nome do Jogador: ')).strip()
gol = str(input('Número de Gols: ')).strip()
x = True
gols = int(gol) if gol.isnumeric() == x else 0
ficha(gols=gols) if nome == '' else ficha(nome, gols)
