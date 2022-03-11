

"""
    Todo arquivo .py é considerao um módulo em python

    O python por padrão transforma todo módulo em um Singleton, ou seja,
    se der import duas vezes no programa não cria duas instâncias
"""

print(f'\n\n')
print(f'----------------------------------------------------------------------------------------------------')

import meu_modulo

meu_modulo.funcao1()

import meu_modulo
import meu_modulo as MM

MM.funcao2()



