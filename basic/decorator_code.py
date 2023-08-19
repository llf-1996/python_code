from functools import wraps


def hint(coder):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            print(f'coder is {coder}')
            return func(*args, **kwargs)
        return inner
    return wrapper


@hint(coder='lisi')
def hello(age, name=None):
    print(f'hello {name}, age({age})')


if __name__ == '__main__':
    print(hello.__name__)
    hello(12, name='world')
    print(hello.__name__)
