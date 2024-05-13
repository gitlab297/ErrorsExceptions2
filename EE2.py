class ZDE(Exception):
    def __init__(self, message, extrainfo):
        self.message = message
        self.extrainfo = extrainfo


class TE(Exception):
    def __init__(self, message, extrainfo):
        self.message = message
        self.extrainfo = extrainfo


def divide_numbers(a, b):
    if b == 0:
        raise ZDE('Делить на ноль нельзя', {'a' : a, 'b' : b})
    if type(b) != int:
        raise TE('Аргументы должны быть числами', {'a' : a, 'b' : b})
    return a / b


a = 7
b = 0
res = None


try:
    result = divide_numbers(a, b)
    res = result
except ZDE as error:
    print('Ошибка. Деление на ноль')
    print(f'Сообщение об ошибке: {error.message}')
    print(f'Дополнительная информация {error.extrainfo}')
except TE as error:
    print('Ошибка. Аргументы должны быть числами')
    print(f'Сообщение об ошибке: {error.message}')
    print(f'Дополнительная информация {error.extrainfo}')
finally:
    print('Результат: ', res)
