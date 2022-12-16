def notas(*num, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    num: uma ou mais notas dos alunos (aceita várias)
    sit: valor opcional, indicando se deve ou não adicionar a situação
    return: dicionário com várias informações sobre a situação da turma.
    '''
    boletim = {}
    boletim['total'] = len(num)
    boletim['maior'] = max(num)
    boletim['menor'] = min(num)
    boletim['média'] = (sum(num) / len(num))
    if sit:
        if boletim['média'] >= 7:
            boletim['situação'] = 'BOA'
        elif boletim['média'] >= 5:
            boletim['situação'] = 'RAZOÁVEL'
        else:
            boletim['situação'] = 'RUIM'
    return boletim


# Programa principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
print(notas.__doc__)
