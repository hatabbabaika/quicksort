import quicksort
import sys
import json


__HELP_CMD__ = 'help'
__SORT_CMD__ = 'sort'

__SHORT_LIST_ARG__ = '-l'
__LIST_ARG__ = '--list'
__LIST_ARGS__ = [__SHORT_LIST_ARG__, __LIST_ARG__]
__SHORT_START_ARG__ = '-s'
__START_ARG__ = '--start'
__START_ARGS__ = [__SHORT_START_ARG__, __START_ARG__]
__SHORT_END_ARG__ = '-e'
__END_ARG__ = '--end'
__END_ARGS__ = [__SHORT_END_ARG__, __END_ARG__]

__HELP_STRING__ = """
Команды
    {sort_cmd} [{list_args}] [{start_args}] [{end_args}] - быстрая сортировка

Аргументы
    {list_args} <items> - массив
    {start_args} <int> - позиция начала сортировки в массиве
    {end_args} <int> - позиция конца сортировки в массиве

Разработал hatabbabaika (Фаттахутдинов Ильнур)
"""


def __help_command__(*args):
    print(__HELP_STRING__.format(
        sort_cmd=__SORT_CMD__,
        list_args='|'.join(__LIST_ARGS__),
        start_args='|'.join(__START_ARGS__),
        end_args='|'.join(__END_ARGS__)
    ))


def __sort_command__(*args):
    list_, start, end = __find_sort_args__(args[1:])
    if not list_:
        print('Не передан сортируемый массив')
    else:
        quicksort.sort(list_, None, start, end)
        print(list_)


def __find_sort_args__(args):
    list_ = []
    start = None
    end = None
    arg_name = None
    for arg in args:
        if arg in [__SHORT_START_ARG__, __START_ARG__, __SHORT_END_ARG__, __END_ARG__, __SHORT_LIST_ARG__, __LIST_ARG__]:
            arg_name = arg
        else:
            if arg_name in __START_ARGS__:
                start = int(arg)
            elif arg_name in __END_ARGS__:
                end = int(arg)
            elif arg_name in __LIST_ARGS__:
                list_.append(arg)
    return list_, start, end


def __unknown_command__(*args):
    print('Неизвестная команда. Аргументы {}'.format(args))


__COMMANDS__ = {
    __HELP_CMD__: __help_command__,
    __SORT_CMD__: __sort_command__
}


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        __COMMANDS__.get(sys.argv[1], __unknown_command__)(*sys.argv[1:])
    else:
        __COMMANDS__[__HELP_CMD__]()
