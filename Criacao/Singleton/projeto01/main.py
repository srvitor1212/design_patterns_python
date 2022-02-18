

import sqlite3


class  Singleton(type):

    __instance = {}

    def __call__(self, *args, **kwargs):
        
        if self not in self.__instance:
            self.__instance[self] = super(Singleton, self).__call__(*args, **kwargs)
        return self.__instance[self]


class Database(metaclass=Singleton):

    connection = None

    def connect(self):
        if self.connection is None:
            print('Não está conectado! Criando conexão...')
            self.connection = sqlite3.connect('db.dadosSingleton')
            self.cursor = self.connection.cursor()
        return self.cursor


print(f'\n\n')
print(f'----------------------------------------------------------------------------------------------------')
db1 = Database().connect()
db2 = Database().connect()