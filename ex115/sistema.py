from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do programa'])
    if resposta == 1:
        #Opção de listar o conteúdo de um arquivo.
        lerArquivo(arq)
    elif resposta == 2:
        #Opção de cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        #Opção de sair do sistema.
        cabeçalho('Saindo do sistema')
        break
    else:
        print('\033[31ERRO! digite uma opção válida!\033[m')
    sleep(1.5)
