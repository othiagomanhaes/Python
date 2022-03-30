from ex115.Lib.Interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') # 'rt' para ler arquivo de texto.
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


# Nessa função o 'wt+' é: (w - write), (t - arquivo de texto), (+ - se o arquivo não existir, ele cria)
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30} {dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at') # 'a' é de appende, ou seja, adcionar informação no arq
    except:
        print('Houve um ERRO na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados.')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
