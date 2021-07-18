from time import sleep, localtime
from biblio.interface.interface import *
from biblio.extras.extras import *
from os import  getcwd, get_terminal_size, listdir, system
from biblio.bib import *

# /* Tamanho Terminal */
tamterm = get_terminal_size()
tamterm = tamterm[0]
if tamterm < 50:
    barra = 2
elif tamterm < 75:
    barra = 4
elif tamterm < 100:
    barra = 6
elif tamterm < 125:
    barra = 8
elif tamterm < 150:
    barra = 10


def abrir(path):
    """
    Tenta abrir o arquivo no caminho que recebe. Caso não encontre o arquivo,
    Cria um arquivo com o nome no caminho especificado.
    :param path: Local onde o arquivo está ou será criado.
    """
    try:
        a = open(path, mode='r')
        return False
    except:
        a = open(path, mode='w+')
        c = 0
        while c < (tamterm-3):
            clear()
            if c < (tamterm-4):
                cabecalho('Criando Arquivo...')
            else:
                cabecalho('Arquivo Criado!')
            cheio = "■" * c
            vazio = "□" * ((tamterm-4) - c)
            print(f'║ {cheio}{vazio} ║', flush=True)
            linhas('╚', '╝', '═', tamterm, flush=True)
            c += barra
            sleep(0.01)
        if c > (tamterm - 9):
            clear()
            cabecalho('Arquivo Criado!')
            cheio = "■" * (tamterm - 4)
            print(f'║ {cheio} ║', flush=True)
            linhas('╚', '╝', '═', tamterm, flush=True)
        input('Enter para Continuar')
    finally:
        a.close()


def ler(path):
    """
    Abre um arquivo no caminho especificado e adiciona o conteudo em uma lista separada pelas linhas do arquivo.
    :param path: Local do arquivo a ser lido.
    """
    try:
        f = open(path, 'tr')
        arquivo = f.readlines()
        f.close()
        abriu = True
    except:
        abriu = False
    if abriu:    
        return arquivo
    else:
        print('Não foi possivel ler o arquivo')
        sleep(1)


def gravar(path, wra, gravacao):
    """
    Abre um arquivo no caminho especificado. Do modo que lhe é definido e adiciona informações a esse arquivo.
    :param path: Local do arquivo onde as informações serão adicionadas.
    :param wra: Modo em que o arquivo será aberto. Sendo: 'r' - leitura, 'w' - escrita, 'a' - adicionar.
    :param gravacao: Conteudo que será salvo no arquivo.
    """
    try:
        f = open(path, wra)
        abriu = True
    except Exception as erro:
        print(f'Não foi possivel devido erro: "{erro.__class__}"')
    if abriu:
        f.write(gravacao)
        f.close()


def adicionar(path):
    """
    Adiciona novos participantes a tabela.
    :param path: Local do arquivo em que o participante será adicionado. 
    """
    try:
        while True:
            es = str(input('Entrada ou Saida? [E/S]: ')).strip().upper()[0]
            if es in 'SE':
                break
            else:
                print('Opção Inválida, Tente novamente!')
                continue
        while True:
            data = leiaInt('Data: ')
            if 0 < data <= 31:
                break
            else:
                print('Data Inválida, Tente novamente!')
                continue
        lancamento = str(input('Lançamento: ')).strip()
        while True:
            try:
                valor = str(input('Valor: R$')).replace(',', '.')
                if valor[:2] == 'R$' or valor[:2] == 'RS':
                    valor = valor[2:]
                valor = float(valor)
            except:
                print('Valor Inválido, Tente novamente!')
                continue
            else:
                break
        gravar(path, 'a', f'{es};{data:0>2};{lancamento};{valor}\n')
    except:
        print('Não foi possivel Adicionar')
    else:
        print(f'"{lancamento}" adicionado com sucesso')
        sleep(1)


def modificar(path, arquivo):
    remover(path, arquivo, False)
    adicionar(path)
    pass


def remover(path, arquivo, rem=True):
    """
    Remove um participante de uma tabela.
    :param path: Local do arquivo a ser modificado.
    :param arquivo: Lista de informações que serão modificadas e gravadas no arquivo.
    """
    if len(arquivo) == 0:
        print('Lista Vazia! Não é possivel remover!')
        input('Enter para continuar')
        return
    pos = leiaInt('Posição: ') - 1
    if -1 < pos <= len(arquivo):
        arquivo[pos] = arquivo[pos].split(';')
        deletado = arquivo[pos][2]
        if rem:    
            while True:
                certeza = str(input(f'Tem Certeza que deseja Remover {deletado}? [S/N]: ')).strip().upper()[0]
                if certeza not in 'SN':
                    print('Escolha Inválida')
                    sleep(2)
                else:
                    break
            if certeza == 'N':
                return
        del arquivo[pos]
        if len(arquivo) == 0:
                    f = open(path, 'w')
                    f.write('')
        else:
            try:
                for p , i in enumerate(arquivo): 
                    if len(arquivo) > 0:
                        if p == 0:
                            f = open(path,'w')
                            f.write(f'{i}')
                        else:
                            f = open(path, 'a')
                            f.write(f'{i}')
            except Exception as erro:
                print(f'Falhao ao Remover da lista em arquivo: {erro.__class__}')
                input('Enter para continuar')
        f.close()
        if rem:
            print(f'{deletado} foi excluido da lista com sucesso!')
            sleep(2)
    else:
        print(f'"{pos+1}" Não faz parte da lista\nRetornando ao Menu Principal...')
        sleep(2)


def pegadata(arquivo):
    return arquivo[1]


def atualizar(path, arquivo):
    arquivo.sort(key=pegadata)
    for p , i in enumerate(arquivo): 
        if len(arquivo) > 0:
            if p == 0:
                f = open(path,'w')
                f.write(f'{i[0]};{i[1]};{i[2]};{i[3]}')
            else:
                f = open(path, 'a')
                f.write(f'{i[0]};{i[1]};{i[2]};{i[3]}')


def limpar(path):
    try:
        gravar(path, 'w', '')
    except:
        print('Não foi possivel limpar o arquivo!')


def delpasta(path):
#    system(f'rmdir /s /q {path}')
    print(path)
    c = 0
    while c < (tamterm - 3):
        clear()
        if c < (tamterm - 4):
            cabecalho('Deletando Pasta...')
        else:
            cabecalho('Pasta Deletada!')
        cheio = "■" * ((tamterm - 4) - c)
        vazio = "□" * c
        print(f'║ {cheio}{vazio} ║', flush=True)
        linhas('╚', '╝', '═', tamterm, flush=True)
        c += barra
        sleep(0.01)
    if c > (tamterm - 9):
        clear()
        cabecalho('Pasta Deletada!')
        vazio = "□" * (tamterm - 4)
        print(f'║ {vazio} ║', flush=True)
        linhas('╚', '╝', '═', tamterm, flush=True)
    input('Enter para Continuar!')


def delarquivo(path):
    """
    Deleta o arquivo do local especificado.
    :param path: Local do arquivo a ser deletado.
    """
    import os
    os.system(f'del {path}')
    c = 0
    while c < (tamterm - 3):
        clear()
        if c < (tamterm - 4):
            cabecalho('Deletando Arquivo...')
        else:
            cabecalho('Arquivo Deletado!')
        cheio = "■" * ((tamterm - 4) - c)
        vazio = "□" * c
        print(f'║ {cheio}{vazio} ║', flush=True)
        linhas('╚', '╝', '═', tamterm, flush=True)
        c += barra
        sleep(0.01)
    if c > (tamterm - 9):
        clear()
        cabecalho('Arquivo Deletado!')
        vazio = "□" * (tamterm - 4)
        print(f'║ {vazio} ║', flush=True)
        linhas('╚', '╝', '═', tamterm, flush=True)
    input('Enter para Continuar!')
    return


def criarpasta(path):
    system(f'mkdir "{path}"')
    c = 0
    while c < (tamterm-3):
        clear()
        if c < (tamterm-4):
            cabecalho('Criando Pasta...')
        else:
            cabecalho('Pasta Criada!')
        cheio = "■" * c
        vazio = "□" * ((tamterm-4) - c)
        print(f'║ {cheio}{vazio} ║', flush=True)
        linhas('╚', '╝', '═', tamterm, flush=True)
        c += barra
        sleep(0.01)
    if c > (tamterm - 11):
        clear()
        cabecalho('Pasta Criada!')
        cheio = "■" * (tamterm - 4)
        print(f'║ {cheio} ║', flush=True)
        linhas('╚', '╝', '═', tamterm, flush=True)
    input('Enter para Continuar')


def lerpasta(pathpasta):
    clear()
    atualpath = getcwd()
    lista = listdir(f'{atualpath}\\{pathpasta}')
    linhas('╔', '╗', '═', tamterm)
    titulo = f'Conteudo de {pathpasta}'
    print(f'║{titulo:^{(tamterm-2)}}║')
    linhas('╠', '╣', '═', tamterm)
    print(f'║{"  [ 0 ] - Voltar a Pasta Principal":{((tamterm//2)-2)}}║{"  [ -1] - Voltar ao Menu Principal":{((tamterm//2))}}║')
    linhas('╟', '╢', '─', tamterm)
    print(f'║{"  [ -2] - Criar Arquivo":{((tamterm//2)-2)}}║{"  [ -3] - Criar Pasta":{((tamterm//2))}}║')
    linhas('╟', '╢', '─', tamterm)
    print(f'║{"  [ -4] - Deletar Arquivo":{((tamterm//2)-2)}}║{"  [ -5] - Deletar Pasta":{((tamterm//2))}}║')
    linhas('╠', '╣', '═', tamterm)
    if len(lista) == 0:
        print(f'║{"":{tamterm - 2}}║')
        print(f'║{"Pasta Vazia":^{tamterm - 2}}║')
        print(f'║{"":{tamterm - 2}}║')
        linhas('╚', '╝', '═', tamterm)
    else:
        for p, c in enumerate(lista):
            print(f'║ {p+1:^3} - {c:<{tamterm - 18}}', end='')
            if c[-3:-1] + c[-1] == 'txt':
                print(f'{"Arquivo":<8} ║')
            else:
                print(f'{"Pasta":<8} ║')
        linhas('╚', '╝', '═', tamterm)
    pasta = leiaInt('Opção: ') - 1
    if pasta == -1:
        arquivo = lerpasta('pastas')
    elif pasta == -2:
        arquivo = 'voltar'
    elif pasta == -3:
        nome = str(input('Nome: '))
        if nome[-4:-1] + nome[-1] != '.txt':
            nome = nome + '.txt'
        nome = atualpath + '/' + pathpasta + '/' + nome
        abrir(nome)
        arquivo = lerpasta(pathpasta)
    elif pasta == -4:
        nome = str(input('nome: '))
        nome = atualpath + '/' + pathpasta + '/' + nome
        criarpasta(nome)
        arquivo = lerpasta(pathpasta)
    elif pasta == -5:
        while True:
            deletar = leiaInt('Arquivo a ser Deletado: ') - 1
            if -1 < deletar < len(lista):
                break
            else:
                print('Opção inválida, Tente Novamente!')
                continue 
        while True:
            confirma = str(input(f'Tem Certeza de que deseja deletar "{lista[deletar]}"? [S/N]: ')).strip().upper()[0]
            if confirma in 'SN':
                break
            else:
                print('Opção Inválida!')
                continue
        if confirma == 'S':
            if lista[deletar][-3:-1] + lista[deletar][-1] == 'txt':
                try:
                    delarquivo(f'{atualpath}\{pathpasta}\{lista[deletar]}')
                except Exception as erro:
                    print(f'Não foi possivel deletar este arquivo!, erro:"{erro.__class__}"')
            else:
                print('Isto é uma pasta, para deletar pastas use outra função!')
                input('Pressione Enter Para Continuar.')
            arquivo = lerpasta(pathpasta)
        elif confirma == 'N':
            arquivo = lerpasta(pathpasta)
    elif pasta == -6:
        while True:
            deletar = leiaInt('Arquivo a ser Deletado: ') - 1
            if -1 < deletar < len(lista):
                break
            else:
                print('Opção inválida, Tente Novamente!')
                continue 
        while True:
            print(f'tem Certeza de que deseja deletar "{lista[deletar]}"')
            confirma = str(input('E Todos os arquivos que contém? [S/N]: ')).strip().upper()[0]
            if confirma in 'SN':
                break
            else:
                print('Opção Inválida!')
                continue
        if confirma == 'S':
            if lista[deletar][-3:-1] + lista[deletar][-1] == 'txt':
                print('Isto é um arquivo, para deletar arquivos use outra função!')
                input('Pressione Enter Para continuar.')
            else:
                try:
#                    delpasta(f'{atualpath}\{pathpasta}\{lista[deletar]}')
                    print(f'{atualpath}\{pathpasta}\{lista[deletar]}')
                except Exception as erro:
                    print(f'Não foi possivel deletar esta pasta!, erro:"{erro.__class__}"')
            arquivo = lerpasta(pathpasta)
        elif confirma == 'N':
            arquivo = lerpasta(pathpasta)
    elif pasta > len(lista) -1 or pasta < -6:
        print('Opção Inválida')
        input('Pressione Enter Para Continuar.')
        arquivo = lerpasta(pathpasta)
    elif lista[pasta][-3:-1] + lista[pasta][-1] == 'txt':
        arquivo = f'{atualpath}\{pathpasta}\{lista[pasta]}'
    else:
        arquivo = lerpasta(f'{pathpasta}\{lista[pasta]}')
    return arquivo


def pastapadrao():
    data = localtime().tm_year, localtime().tm_mon
    atualpath = getcwd() + '\pastas\\'
    mes = ['01-Janeiro.txt','02-Fevereiro.txt','03-Março.txt',
         '04-Abril.txt','05-Maio.txt','06-Junho.txt',
         '07-Julho.txt','08-Agosto.txt','09-Setembro.txt',
         '10-Outubro.txt','11-Novembro.txt','12-Dezembro.txt']
    try:
        arquivo = f'{atualpath}{data[0]}\{mes[data[1]-1]}'
        open(arquivo, 'r')
    except:
        try:
            system(f'mkdir "{atualpath}{data[0]}"')
            for p, c  in enumerate(mes):
                arquivo = f'{atualpath}{data[0]}\{mes[p]}'
                try:
                    a = open(arquivo, 'r')
                except:    
                    a = open(arquivo, 'w+')
                a.close()
        except Exception as erro:
            print(f'Não Foi possivel devido ao erro: "{erro.__class__}"')
    arquivo = f'{atualpath}{data[0]}\{mes[data[1]-1]}'
    return arquivo