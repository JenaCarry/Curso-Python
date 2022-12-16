from colorful import gn, pk, rd, nn
n = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {pk}{type(n)}{nn}!')
print(f'Só tem espaços?{gn}' if n.isspace() is True else f'Só tem espaços?{rd}', n.isspace(), nn)  # noqa
print(f'É um número?{gn}' if n.isnumeric() is True else f'É um número?{rd}', n.isnumeric(), nn)  # noqa
print(f'É alfabético?{gn}' if n.isalpha() is True else f'É alfabético?{rd}', n.isalpha(), nn)  # noqa
print(f'É alfanumérico?{gn}' if n.isalnum() is True else f'É alfanumérico?{rd}', n.isalnum(), nn)  # noqa
print(f'Está em maiúscula?{gn}' if n.isupper() is True else f'Está em maiúscula?{rd}', n.isupper(), nn)  # noqa
print(f'Está em minúscula?{gn}' if n.islower() is True else f'Está em minúscula?{rd}', n.islower(), nn)  # noqa
print(f'Está capitalizada?{gn}' if n.istitle() is True else f'Está capitalizada?{rd}', n.istitle(), nn)  # noqa
print(gn if n.isascii() is True else rd, n.isascii(), nn)
print(gn if n.isdecimal() is True else rd, n.isdecimal(), nn)
print(gn if n.isdigit() is True else rd, n.isdigit(), nn)
print(gn if n.isidentifier() is True else rd, n.isidentifier(), nn)
print(gn if n.isprintable() is True else rd, n.isprintable(), nn)
