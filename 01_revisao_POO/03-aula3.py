

from statistics import mode
from typing import List, Tuple


class Curso:

    def __init__(self: object, nome:str='Curso Padrão', carga_horaria:int=45) -> None:
        self.__nome = nome
        self.__carga_horaria = carga_horaria


print(f'\n\n')
print(f'----------------------------------------------------------------------------------------------------')
print(f'>>> Exemplos de uso')
curso1: Curso = Curso()
curso2: Curso = Curso(nome='Padrões de projeto python')
curso3: Curso = Curso(nome='Container com kubernets', carga_horaria=23)
print(curso1.__dict__)
print(curso2.__dict__)
print(curso3.__dict__)

print(f'----------------------------------------------------------------------------------------------------')
print(f'>>> seggunda parte')
nome: str = 'Geek universety'
tupla: Tuple = (1,2,3,4,5)
lista: List = [1,2,3,4,5]

print(nome[:3], tupla[:3], lista[:3])

print(f'----------------------------------------------------------------------------------------------------')
print(f'>>> terceira parte')

class Pessoa:

    def __init__(self:object, nome:str) -> None:
        self.__nome = nome

    def andar(self:object):
        print('Estou andando...')

class Aluno(Pessoa):

    def __init__(self: object, nome: str, matricula: str) -> None:
        super().__init__(nome)
        self.__matricula = matricula


vitor = Aluno('Vitor Vicente', 'mat00932')
print(f'>> Vitor [{vitor.__dict__}]')
vitor.andar()


print(f'----------------------------------------------------------------------------------------------------')
print(f'>>> quarta parte')

# Abstração, a pessoa não precisa saber da complexidade, só usar a função e pronto
def calcular(qtd:int) -> None:
    if qtd <= 0:
        print('Não pode ser menor que zero')
    else:
        print(f'Valor calculado é: {((qtd + 10) / 100)}')

calcular(4)

print(f'----------------------------------------------------------------------------------------------------')
print(f'>>> quinta parte')

class Motor:
    def ligar(self:object) -> None:
        print('Motor ligado')

class Pneu:
    def encher(self:object) -> None:
        print('Pneu cheio')

class Carro:
    def __init__(self:object, modelo:str) -> None:
        self.__modelo = modelo
        self.__motor = Motor() # Isso é composição, não erada mas usa
        self.__pneu1 = Pneu()
        self.__pneu2 = Pneu()
        self.__pneu3 = Pneu()
        self.__pneu4 = Pneu()


fusca = Carro('Ford')
fusca._Carro__motor.ligar()  # da para acessar os atributos assim, chama-se numlink

print(f'>> fusca dict [{fusca.__dict__}]')
