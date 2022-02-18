

"""
    Todo arquivo .py é considerao um módulo em python

    O python por padrão transforma todo módulo em um Singleton, ou seja,
    se der import duas vezes no programa não cria duas instâncias
"""


def funcao1():
    print('Função 01')

def funcao2():
    print('Função 02')


NOME = 'Geek Universety'    # nome maiusculo pra dizer que é constante
print(f'Módulo importado...')