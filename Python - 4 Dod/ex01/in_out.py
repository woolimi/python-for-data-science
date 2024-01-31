def square(x: int | float) -> int | float:
    """
    Get square of x
    """
    return x ** 2


def pow(x: int | float) -> int | float:
    """
    Get power of x
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Get a function that calculate and update its inner value
    """
    count = x

    def inner() -> float:
        nonlocal count
        count = function(count)
        return count

    return inner
