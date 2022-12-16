def voto(ano):
    from datetime import datetime
    '''Mostra se uma pessoa tem idade para votar.'''
    idade = datetime.now().year - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


print('-' * 30)
nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))
