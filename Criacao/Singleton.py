

"""
    O padrão de projeto Singleton é um dos padrões de projetos mais simples e conhecidos no mundo 
    da programação. 
    
    O Singleton proporciona uma forma de ter um, e somente um, objeto de determinado 
    tipo, além de um ponto de acesso global à este objeto.
"""


class Singleton:

    def __new__(cls):       # new é executado antes mesmo do __init__, new que cria o objeto
        
        if not hasattr(cls, 'instance'):        # se não existe o atriburo instance em 'cls'
            cls.instance = super(Singleton, cls).__new__(cls)   # instância a classe através do método __new__
            print(f'Criando o objeto [{cls.instance}]')

        print(f'Já tem uma instância criada')
        return cls.instance



print(f'\n\n')
print(f'----------------------------------------------------------------------------------------------------')
s1 = Singleton()
print(f'Instância 1 : [{id(s1)}]')

s2 = Singleton()
print(f'Instância 2 : [{id(s2)}]')

s3 = Singleton()
print(f'Instância 3 : [{id(s3)}]')
