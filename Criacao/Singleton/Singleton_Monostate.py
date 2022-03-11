

"""
    State é estado, em python os atributos são os estados da classe

    Monostate vamos ter instâncais diferente da classe, só que em mesmo estado
"""


class Monostate:

    __estado = {}

    def __new__(cls, *args, **kargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kargs)
        obj.__dict__ = cls.__estado
        return obj


print(f'\n\n')
print(f'----------------------------------------------------------------------------------------------------')
m1 = Monostate()
print(f'M1 ID: [{id(m1)}]')
print(m1.__dict__)

m2 = Monostate()
print(f'M2 ID: [{id(m2)}]')
print(m1.__dict__)

m1.nome = 'Vitor Vicente'
print(f'm1 dict [{m1.__dict__}]')
print(f'm2 dict [{m2.__dict__}]')