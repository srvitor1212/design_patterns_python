

class University(type):

    def __call__(cls, *args, **kwargs):      # quando instancia Geek, chama o método call da University
        print(f'>>> Esses são os args: [{args}]')
        print(f'>>> Esses são os kargs: [{kwargs}]')
        return type.__call__(cls, *args, **kwargs)


class Geek(metaclass=University):

    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2


print(f'\n\n')
print(f'----------------------------------------------------------------------------------------------------')
obj = Geek(42, 23)
print(obj)