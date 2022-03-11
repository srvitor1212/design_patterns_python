

from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):

    @abstractmethod
    def falar(self):
        pass

class Cachorro(Animal):

    def falar(self):
        print('Au Au')

class Gato(Animal):

    def falar(self):
        print('Miau')

# ----------- Fábrica
class Factory:

    def criar_animal(self, tipo):
        return eval(tipo)()     # eval = avalia a string recebida e tenta executar como comando python


print(f'\n\n')
print(f'----------------------------------------------------------------------------------------------------')

fab = Factory()
animal = input('Escolha um animal [Cachorro] ou [Gato] ')
obj = fab.criar_animal(animal)
obj.falar()