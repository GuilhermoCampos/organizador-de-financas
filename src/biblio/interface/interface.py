from biblio.extras.extras import *
from biblio.arquivo.arquivo import *
from biblio.interface.interface import *
from os import get_terminal_size, system, getlogin
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



def linhas(inicio, fim , simb, tam, end='\n', flush=False):
    """
    Cria uma sequência de simbolos formando uma linha
    :param inicio: Caractere que será utilizado na primeira posição da linha.
    :param fim: Caractere que será utilizado na última posição da linha.
    :param simb: Simbolo que será utilizado em todo o restante da linha.
    :param tam: Tamanho total que a linha terá.
    :param end: Função que define como a linha irá terminar. O padrão é '\n' para que 
    o proximo print seja feito uma linha abaixo.
    :param flush: Define se a atualização do print será constante.
    """
    lin = simb * (tam - 2)
    print(inicio, end='')
    print(f'{lin}', end='')
    print(fim)


def cabecalho(titulo, supe='╔', supd='╗', infe='╠', infd='╣'):
    """
    Cria um cabeçalho padrão com um titulo personalizavel.
    :param titulo: Titulo do cabeçalho.
    """
    linhas(supe, supd, '═', tamterm)
    print(f'║{titulo:^{tamterm - 2}}║')
    linhas(infe, infd, '═', tamterm)


def menu(lista, ver='', supe='╔', supd='╗', infe='╠', infd='╣'):
    """
    Cria um menu com todas as opções que forem adicionadas a lista.
    :param lista: Lista com todas as opções que serão mostradas no menu.
    :param ver: Versão atual do programa que será exibido no canto inferior direito do menu.
    """
    cabecalho('Menu Principal', supe, supd, infe, infd)
    for p, i in enumerate(lista):
        if i == lista[-1]:
            print(f'║ {p+1} - {i:<{tamterm - 18}}{ver:>10} ║')
        else:    
            print(f'║ {p+1} - {i:<{tamterm - 7}}║')
    linhas('╚', '╝', '═', tamterm)
    opc = leiaInt('Escolha uma Opção: ')
    return opc


def menuArquivo():
    system('title Tabela de Finanças')
    system('color 0a')
    clear()
    nome = getlogin()
    msg = f'Seja bem Vindo {nome}'
    linhas('╔', '╗', '═', tamterm)
    print(f'║{msg:^{tamterm - 2}}║')
    linhas('╠', '╣', '═', tamterm)
    print(f'║{"Opções":^{tamterm-2}}║')
    linhas('╠', '╣', '═', tamterm)
    print(f'║{" 1 - Abrir um Arquivo Padrão":^{(tamterm//2) - 2}}║{" 2 - Navegar Pelas Pastas":^{((tamterm//2))}}║')
    linhas('╚', '╝', '═', tamterm)
    opc = leiaInt('Opção: ')
    return opc


def organizar(arquivo):
    """
    Organiza os itens de um arquivo em uma lista.
    :param arquivo: Arquivo a ser organizado em uma lista.
    """
    lista = list()
    if len(arquivo) > 0:
        for linha in arquivo:
            dado = linha.split(';')
            lista.append(dado[:])
    return lista


def mostrar(lista, nome):#path
    """
    Mostra uma lista organizada dos participantes. Com a Posição, O Nome e a Pontuação atual do participante.
    :param lista: Lista que será mostrada.
    """
    cabecalho(nome)
    print(f'║{"  [ 1 ] - Adicionar Item":^{((tamterm//2)-2)}}║{"  [ 2 ] - Modificar Item":^{((tamterm//2))}}║')
    linhas('╟', '╢', '─', tamterm)
    print(f'║{"  [ 3 ] - Remover Item  ":^{((tamterm//2)-2)}}║{"  [ 4 ] - Limpar Arquivo":^{((tamterm//2))}}║')
    linhas('╟', '╢', '─', tamterm)
    print(f'║{"  [ 5 ] - Retornar      ":^{((tamterm//2)-2)}}║{"  [ 6 ] - Sair          ":^{((tamterm//2))}}║')
    linhas('╠', '╣', '═', tamterm)
    print(f'║ {"POS":>3} ║ {"E/S":^3} ║ {"DATA":^6} ║ {"       Lançamentos":^{tamterm-55}} ║ {"Valor":^12} ║ {"Saldo":^12} ║')
    linhas('╠', '╣', '═', tamterm)
    if len(lista) == 0:
        print(f'║{"":{tamterm - 2}}║')
        linhas('╟', '╢', '─', tamterm)
        print(f'║{"Tabela Vazia":^{tamterm - 2}}║')
        linhas('╟', '╢', '─', tamterm)
        print(f'║{"":{tamterm - 2}}║')
    saldo = ent = sai = salatu = mov = 0
    for p, c in enumerate(lista):
        mov += 1
        c[3] = float(c[3])
        # if p == 0:
            #print(organizar(pastapadrao(True))[-1][3])
        if c[0] == 'S':
            saldo = saldo - c[3]
            sai += c[3]
        elif c[0] =='E':
            saldo = saldo + c[3]
            ent += c[3]
        if p == 0:
            c[3] = str(f'{c[3]:.2f}').replace('.', ',')
            saldo = str(f'{saldo:.2f}').replace('.', ',')
            print(f'║ {p+1:^3} ║ {c[0]:^3} ║ Dia {c[1]:0>2} ║ {c[2]:<{tamterm-55}} ║ R${c[3]:<10} ║ R${saldo:<10} ║')
            saldo = saldo.replace(',', '.')
            saldo = float(saldo)
        else:
            c[3] = str(f'{c[3]:.2f}').replace('.', ',')
            saldo = str(f'{saldo:.2f}').replace('.', ',')
            linhas('╟', '╢', '─', tamterm)
            print(f'║ {p+1:^3} ║ {c[0]:^3} ║ Dia {c[1]:0>2} ║ {c[2]:<{tamterm-55}} ║ R${c[3]:<10} ║ R${saldo:<10} ║')
            saldo = saldo.replace(',', '.')
            saldo = float(saldo)
    salatu = ent - sai
    ent = str(f'{ent:.2f}').replace('.', ',')
    sai = str(f'{sai:.2f}').replace('.', ',')
    salatu = str(f'{salatu:.2f}').replace('.', ',')
    entrada = f'Total de Entradas: R${ent:<10}'
    saidas = f'Total de Saidas: R${sai:<10}'
    saldo_atual = f'Saldo Atual: R${salatu:<10}'
    movimentacoes = f'Movimentações :{mov:<6}'
    linhas('╠', '╣', '═', tamterm)
    print(f'║ {entrada:30} ║ {saidas:29} ║ {saldo_atual:{(tamterm-99)}} ║ {movimentacoes} ║') #81
    linhas('╚', '╝', '═', tamterm)
    opc = leiaInt('Opção: ')
    return opc
