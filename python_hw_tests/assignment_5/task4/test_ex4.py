def flatten(nested: list) -> list:
    """
    >>> flatten([1, 2, [4, [8, 9, [11, 12], 10], 5], 3, [6, 7]])
    [1, 2, 4, 8, 9, 11, 12, 10, 5, 3, 6, 7]
    >>> flatten([[]])
    []
    >>> flatten([[], [], [1], [], [1, [], [4, 5, [[[6]]]], 2, 3]])
    [1, 1, 4, 5, 6, 2, 3]
    """
    if len(nested)==0:
        return []
    else:
        if isinstance(nested[0],list):
            return flatten(nested[0])+flatten(nested[1:])
        else:
            return nested[:1]+flatten(nested[1:])


if __name__=='__main__':
    import doctest
    doctest.testmod()