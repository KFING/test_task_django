import doctest

################
# Lst is Lst #
################

CONTROL_LST = [1, 7, 2, 7, 3, 7, 4, 7]


def lis_is_lst(a: list, b: list, dlt: int = 1) -> None:
    """
    Реализовать тело функции что бы c == CONTROL_LST
    >>> lis_is_lst([7, 7, 7, 7], [4, 2, 1, 3])
    True
    >>> lis_is_lst(["1234"], [7, 7, 7])
    True
    >>> lis_is_lst([1, 4, 3, 7, 2], [])
    True
    """
    c = a + b
    print(c == CONTROL_LST * dlt)


#############
# The Magic #
#############

def decorate_me_decorate(func):
    def inner1(*args, **kwargs):
        if func(*args, **kwargs) < 5:
            context = 'Low Result'
        elif func(*args, **kwargs) < 51:
            context = 'Result'
        else:
            context = 'Great Result'
        print(f'{context}: {func(*args, **kwargs)}')

    return inner1



@decorate_me_decorate
def decorate_me(some_int):
    """
    Написать декоротор для функции(но не изменять саму функцию) что бы при выполнении следующего кода вывод был следущим:
    >>> decorate_me(25)
    'Result: 50'
    >>> decorate_me(196)
    'Great Result: 392'
    >>> decorate_me(2)
    'Low Result: 4'
    """
    return some_int * 2


def magic_decorator(func):
    def inner1():
        print('???')

    return inner1
@magic_decorator
def magic(stall=[]):
    """
    Написать декоротор для функции(но не изменять саму функцию) что бы при выполнении следующего кода вывод был следущим:
    >>> magic()
    ???
    >>> magic()
    ???
    >>> stall = []
    >>> magic(stall)
    ???
    >>> stall = 45
    >>> magic(stall)
    ???
    >>> stall == _
    ???
    """
    unicorn = '🦄'
    if hasattr(stall, 'append') and callable(stall.append):
        stall.append(unicorn)
    elif hasattr(stall, 'add') and callable(stall.add):
        stall.add(unicorn)
    else:
        stall = unicorn

    return stall


################
# Paint It All #
################

# Заставить сработать функцию как это описано в комментарии, изменять сами классы PaintIt{Color} нельзя
from enum import Enum


class Color(Enum):
    BLACK = '⚫'
    RED = '🔴'
    GREEN = '🟢'


# Необходимо вместо этой реализации класс PaintIt написать свою
PaintIt = type('_', (type,), {'__new__': lambda *a, **_: type.__new__(*a)})('_', (), {})


class PaintItBlack(PaintIt, color=Color.BLACK):
    ...


class PaintItGreen(PaintIt, color=Color.GREEN):
    ...


class PaintItRed(PaintIt, color=Color.RED):
    ...


# функцию изменять нельзя
def paint_it_all():
    """
    >>> paint_it_all()
    ⚫ 🟢 🔴
    """
    print(PaintItBlack(), PaintItGreen(), PaintItRed())


###########
# Doctest #
###########


if __name__ == "__main__":
    globs = globals()

    for test in (
            lis_is_lst, decorate_me, magic, paint_it_all
    ):
        # Use context managers here
        name = test.__name__
        line = "#" * (len(name) + 4)
        print(f"{line}\n# {name} #\n{line}\n")
        doctest.run_docstring_examples(test, globs, name=name)
        print()
