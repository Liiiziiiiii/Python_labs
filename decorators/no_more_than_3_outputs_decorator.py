from functools import wraps


def no_more_than_3_outputs_decorator(func):
    count = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1

        if count > 3:
            count = 0

            raise ValueError("Too many calls")

        return func(*args, **kwargs)

    print("valid output value")

    return wrapper
