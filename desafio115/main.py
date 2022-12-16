from lib.interface import menu, cabeçalho, leia_int
from time import sleep
from lib.arquivo import arquivo_exite, criar_arquivo, ler_arquivo, cadastrar

arquivo = 'enquete.txt'

if not arquivo_exite(arquivo):
    criar_arquivo(arquivo)

while True:
    resp = menu(['Ver pessoas Cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])  # noqa
    if resp == 1:
        # Opção de listar o conteúdo de um arquivo
        ler_arquivo(arquivo)
    elif resp == 2:
        # Opção de cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip().title()
        idade = leia_int('Idade: ')
        cadastrar(arquivo, nome, idade)
    elif resp == 3:
        cabeçalho('Saindo do Sistema... Até logo!')
        break
    else:
        cabeçalho('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1.5)
