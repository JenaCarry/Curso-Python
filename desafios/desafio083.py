expressão = str(input('Digite uma expressão: '))
parenteses = []
for simb in expressão:
    if simb == '(':
        parenteses.append('(')
        print(parenteses)
    elif simb == ')':
        if len(parenteses) > 0:
            parenteses.pop()
            print(parenteses)
if len(parenteses) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')
