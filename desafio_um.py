"""

Desafio 1:

Algoritmo que mostre na tela uma escada de tamanho n utilizando o caractere * e espaços.
A base e altura da escada devem ser iguais ao valor de n.
A última linha não deve conter nenhum espaço.

"""

def mostrar_escada(n):
    """Função criada para mostrar a escada"""
    space = n - 1
    for i in range(n):
        for j in range(space):
            print(' ', end='')
        for j in range(n - space):
            print('*', end='')
        space = space - 1
        print()
    print()
#PROGRAMA

print("~~~~~~~~~~~~  DESAFIO 1  ~~~~~~~~~~~~~~\n")

n=int(input("Digite o tamanho da escada (degraus) que você deseja que apareça na tela: "))
mostrar_escada(n)