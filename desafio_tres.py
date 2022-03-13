"""
Desafio 3:

Dada uma string qualquer, desenvolva um algoritmo que encontre o número de pares de substrings que são anagramas.

"""

def encontrar_pares_substrings_anagramas(substr):
    """Função criada para encontrar o número de pares de substrings que são anagramas"""
    n = len(substr)
    dici = dict()

    # for para o tamanho da substring
    for i in range(n):
        x = ''
        for h in range(i, n):
            x = ''.join(sorted(x + substr[h]))
            dici[x] = dici.get(x, 0)
            dici[x] += 1

    # Realização da contagem
    anagr = 0
    for k, y in dici.items():
        anagr += (y * (y - 1)) // 2
    return anagr


# PROGRAMA

substr = input("Olá!\nDigite a string que você deseja encontrar o número de pares de substrings que são anagramas: ")
print(
    f'\nO número de pares de substrings da string que você digitou é:\n~~~~~~~~~~~~~~  {encontrar_pares_substrings_anagramas(substr)}  ~~~~~~~~~~~~~~')
