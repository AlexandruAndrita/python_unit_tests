def binary_search(elements: list,x) -> bool:
    """
    >>> my_list=[1, 2, 5, 7, 8, 10, 20, 30, 41, 100]
    >>> binary_search(my_list,1)
    True
    >>> binary_search(my_list,20)
    True
    >>> binary_search(my_list, 21)
    False
    >>> binary_search(my_list, "Hello")
    False
    >>> binary_search([], 22)
    False
    """

    if len(elements)==0:
        return False
    if len(elements)==1 and elements[len(elements)-1]!=x:
        return False
    if elements[len(elements)//2]==x:
        return True
    try:
        if elements[len(elements)//2]<x:
            return binary_search(elements[len(elements)//2:],x)
        else:
            return binary_search(elements[:len(elements)//2], x)
    except TypeError:
        return False


if __name__=='__main__':
    import doctest
    doctest.testmod()