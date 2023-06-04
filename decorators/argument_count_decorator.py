from functools import wraps
import logging


def argument_count_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        arg_count = len(args) + len(kwargs)
        print(f"Method '{func.__name__}' called with {arg_count} arguments.")
        return func(*args, **kwargs)

    return wrapper


def convert_iterator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return tuple(result)

    return wrapper


def logged(exception, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                if mode == "console":
                    logging.basicConfig(level=logging.INFO)
                elif mode == "file":
                    logging.basicConfig(filename='error.log', filemode='a', level=logging.INFO)
                logging.exception(e)

        return wrapper

    return decorator
