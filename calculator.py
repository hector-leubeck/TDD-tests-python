

def sum(x, y):
    """
    >>> sum(10, 20)
    30
    >>> sum(10, 20.5)
    30.5
    >>> sum(-10, 20)
    10
    >>> sum(10, -20)
    -10
    >>> sum(-1.5, 2)
    0.5
    """
    return x + y


def subtract(x: float | int, y: int | float):
    """
    >>> subtract(10, 20)
    -10
    >>> subtract(10, 20.5)
    -10.5
    >>> subtract(-10, 20)
    -30
    >>> subtract(10, -20)
    30
    >>> subtract(-1.5, 2)
    -3.5
    """
    return x - y


def multiply(x: float | int, y: int | float):
    """
    >>> multiply(10, 20)
    200
    >>> multiply(10, 20.5)
    205.0
    >>> multiply(-10, 20)
    -200
    >>> multiply(10, -20)
    -200
    >>> multiply(-1.5, 2)
    -3.0
    """
    return x * y


def divide(x: float | int, y: int | float):
    """
    >>> divide(10, 20)
    0.5
    >>> divide(10, 2.5)
    4.0
    >>> divide(-10, 20)
    -0.5
    >>> divide(10, -20)
    -0.5
    >>> divide(-1.5, 5)
    -0.3
    """
    return x / y


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
