

class MetaSingleton(type):

    __instance = {}

    def __call__(self, *args, **kwargs):
        if self not in self.__instance:
            self.__instance[self] = super(MetaSingleton, self).__call__(*args, **kwargs)
        return self.__instance[self]


class Logger(metaclass=MetaSingleton):
    pass


print(f'\n\n')
print(f'----------------------------------------------------------------------------------------------------')

log1 = Logger()
print(f'log1 [{id(log1)}]')

log2 = Logger()
print(f'log2 [{id(log2)}]')


