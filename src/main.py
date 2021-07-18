from biblio.bib import *

# Programa
while True:
    # Menu Inicial
    while True:
        opc = menuArquivo()
        if opc == 1:
            arquivo = pastapadrao()
            break
        elif opc == 2:
            arquivo = lerpasta('pastas')
            if arquivo == 'voltar':
                continue
            else:
                break
    atualpath = getcwd() + '\pastas\\'
    nome = arquivo[len(atualpath):-4].replace('\\', ' ').title()
    # Menu Principal
    while True:
        clear()
        atualizar(arquivo, organizar(ler(arquivo)))
        opc = mostrar(organizar(ler(arquivo)), nome)
        if opc == 1:
            adicionar(arquivo)
            atualizar(arquivo, organizar(ler(arquivo)))
        elif opc == 2:
            modificar(arquivo, ler(arquivo))
        elif opc == 3:
            remover(arquivo, ler(arquivo))
        elif opc == 4:
            while True:
                confirma = str(input('Deseja APAGAR todos os dados deste arquivo?[S/N]: ')).strip().upper()[0]
                if confirma in 'SN':
                    break
                else:
                    print('Opção Inválida, Tente novamente!')
                    continue
            if confirma == 'S':
                limpar(arquivo)
            elif confirma == 'N':
                continue
        elif opc == 5:
            continua = 'voltar'
            break
        elif opc == 6:
            continua = 'fechar'
            break
        continue
    if continua == 'voltar':
        continue
    elif continua == 'fechar':
        break
