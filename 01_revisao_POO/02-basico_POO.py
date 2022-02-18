

from datetime import datetime


class Pessoa:

    def __init__(self: object, nome: str) -> None:
        self.__nome = nome              # o dunder __ torna o atributo privado
        self.teste = 'teste atributo'   # assim é publico, da  pra usar Pessoa.teste
        self.__nascimento = datetime.now()

    def __str__(self: object) -> str:
        return self.__nome

    def __repr__(self: object) -> str:
        return self.__nome


class Carro:

    def __init__(self: object, is_sedan: bool = False) -> None:
        self.__is_sedan = is_sedan
        self.__velocidade = 0
        self.__motorista = None

    def __str__(self: object) -> str:
        if self.__motorista:
            return f'Carro do(a) {self.__motorista}'
        return f'Carro sem motorista'
    
    @property
    def motorista(self):
        return self.__motorista

    def dirigir(self: object, motorista: Pessoa) -> None:
        self.__motorista = motorista
        self.acelerar(1)

    def acelerar(self: object, velocidade: int) -> None:
        self.__velocidade += velocidade

    def parar(self: object):
        self.__velocidade = 0


print(f'\n\n')
print(f'----------------------------------------------------------------------------------------------------')
print(f'>>> Exemplos de uso')

vitor = Pessoa('Vitor Vicente')
print(f'Pessoa >> [{vitor}]')
fusca = Carro()
print(f'Carro >> [{fusca}]')

print(f'Carro.dirigir >> [{fusca.dirigir(vitor)}]')
print(f'Carro.__dict__ >> [{fusca.__dict__}]')
print(f'type motorista do carro >> [{type(fusca.motorista)}]') # Uma classe "dentro" da outra

print(f'atributo sem dunder >> [{vitor.teste}]')