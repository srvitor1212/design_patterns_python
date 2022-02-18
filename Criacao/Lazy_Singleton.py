

class Singleton:

    __instance = None

    def __init__(self) -> None:
        if not Singleton.__instance:
            print('O método __init__ foi chamado...')
        else:
            print(f'A instância já foi criada [{self.get_instance()}]')

    
    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
            print('Criou instância')
        return cls.__instance


print(f'\n\n')
print(f'----------------------------------------------------------------------------------------------------')

print(f'\n >>> ponto 1')
s1 = Singleton()            # A classe é iniciada mas o objeto não é criado

print(f'\n >>> ponto 2')
Singleton.get_instance()    # Cria a instância

print(f'\n >>> ponto 3')
s2 = Singleton()            # Instância já criada