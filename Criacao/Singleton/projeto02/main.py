

class SanidadeCheck:

    __instance = None

    def __new__(cls, *args, **kwargs):
        if not SanidadeCheck.__instance:
            SanidadeCheck.__instance = super(SanidadeCheck, cls).__new__(cls, *args, **kwargs)
        return SanidadeCheck.__instance

    def __init__(self) -> None:
        self.__servidores = []

    def checar_servidor(self, server):
        print(f'Check servidor {self.__servidores[server]}')

    def add_servidor(self):
        self.__servidores.append('Server 001')
        self.__servidores.append('Server 002')
        self.__servidores.append('Server 003')
        self.__servidores.append('Server 004')

    def mudar_servidor(self):
        self.__servidores.pop()
        self.__servidores.append('Server 005')


print(f'\n\n')
print(f'----------------------------------------------------------------------------------------------------')

sc1 = SanidadeCheck()
sc2 = SanidadeCheck()
sc1.add_servidor()

print('>>> Checagem de servidores, A ...')
for srv in range(4):
    sc1.checar_servidor(srv)
sc2.mudar_servidor()

print('>>> Checagem de servidores, B ...')
for srv in range(4):
    sc2.checar_servidor(srv)