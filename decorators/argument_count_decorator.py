from functools import wraps


def argument_count_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        arg_count = len(args) + len(kwargs)
        print(f"Method '{func.__name__}' called with {arg_count} arguments.")
        return func(*args, **kwargs)

    return wrapper
