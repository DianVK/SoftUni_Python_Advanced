def type_check(expected_type):
    def decorator(func):
        def wrapper(arg):
            if not isinstance(arg, expected_type):
                return "Bad Type"
            return func(arg)

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))
