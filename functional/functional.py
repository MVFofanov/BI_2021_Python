def sequential_map(*args):
    *functions, numbers = args
    final_func = func_chain(*functions)
    result = list(map(final_func, numbers))
    return result


def consensus_filter(*args):
    *functions, numbers = args
    result = numbers
    for func in functions:
        result = list(filter(func, result))
    return result


def conditional_reduce(logic_func, func, numbers):
    result, *numbers = list(filter(logic_func, numbers))
    for number in numbers:
        result = func(result, number)
    return result


def func_chain(*args):
    def final_func(number):
        for func in args:
            number = func(number)
        return number
    return final_func
