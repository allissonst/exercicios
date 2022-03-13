"""

Desafio 2:

Construa um algoritmo que informe qual é o número mínimo de caracteres que devem ser adicionados
para uma string qualquer ser considerada segura.

Observação: Além do que foi solicitado pelo desafio, inclui todos os critérios de validação elencados na
situação-problema

"""

def mostrar_criterios_senha_forte(nome):
    print(f'Olá {nome}!\nUma senha forte em redes sociais possui: \n')
    print("- No mínimo 6 caracteres;")
    print("- Contém no mínimo 1 dígito;")
    print("- Contém no mínimo 1 letra em minúsculo;")
    print("- Contém no mínimo 1 letra em maiúsculo;")
    print("- Contém no mínimo 1 caractere especial: !@#$%^&*()-+")

def verificar_senha(senha_forte, caracteres_especiais, digitos, tam_senha_forte):
    """Função criada para verificar se a senha é forte"""
    while senha_forte == False:
        senha = input("\nDigite uma senha para testar se é forte:")
        if not any(x.isupper() for x in senha) or len(senha) < tam_senha_forte or not any(x.islower() for x in senha) or not any(
                c in caracteres_especiais for c in senha) or not any(c in digitos for c in senha):

            if not any(x.isupper() for x in senha):
                print("Sua senha precisa ter ao menos uma letra maiúscula")

            if len(senha.lstrip()) < 6:
                print(
                    f'Sua senha precisa ter no mínimo {tam_senha_forte} caracteres. Faltam {tam_senha_forte - len(senha.lstrip())} caracteres para atingir a quantidade mínima.')

            if not any(x.islower() for x in senha):
                print("Sua senha precisa ter ao menos uma letra minúscula")

            if not any(c in digitos for c in senha):
                print("Sua senha precisa ter ao menos um número de 0 a 9")

            if not any(c in caracteres_especiais for c in senha):
                print("Sua senha precisa ter ao menos um caractere especial: !@#$%^&*()-")

        else:
            senha_forte = True
            print(f'\nVocê encontrou uma senha forte {nome}!\nParabéns!!!')

    print()

#PROGRAMA
print("~~~~~~~~~~~~  DESAFIO 2 ~~~~~~~~~~~~~~\n")

caracteres_especiais = "!@#$%^&*()-+"
digitos = "0123456789"
tam_senha_forte = 6
senha_forte = False

nome = input("Digite seu nome: ")
mostrar_criterios_senha_forte(nome)
verificar_senha(senha_forte=senha_forte, caracteres_especiais=caracteres_especiais, digitos=digitos,
                tam_senha_forte=tam_senha_forte)
