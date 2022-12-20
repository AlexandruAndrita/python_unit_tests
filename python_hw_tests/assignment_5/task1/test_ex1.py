def fib(n: int) -> int:
    """
    >>> fib(0)
    0
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(20)
    6765
    >>> fib(34)
    5702887
    >>> fib(-100)
    -1
    """

    if n<0:
        return -1
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)


if __name__=='__main__':
    import doctest
    doctest.testmod()
