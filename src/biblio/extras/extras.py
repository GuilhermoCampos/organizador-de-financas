from os import system


def leiaInt(txt):
    """
    Aceitando apenas que o usuário adicione um valor inteiro, caso não seja inserido um valor inteiro,
    é soliciado novamente que o Usuário digite um número que não está na lista o menu é recarregado adicione um valor inteiro.
    :param txt: Texto a ser exibido solicitando os dados do Usuário digite um número que não está na lista o menu é recarregado.
    """
    while True:
        try:
            num = int(input(txt))
        except:
            print('Por favor insira um número inteiro válido')
            continue
        else:
            return num
        

def clear():
    """
    Limpa o prompt de comando.
    """
    import os
    system('cls')

