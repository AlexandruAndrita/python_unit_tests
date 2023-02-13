def special_case(start: int,stop: int,step: int=1):
    if start>=stop:
        return []
    return [start]+special_case(start-step,stop,step)


def gen_range(start: int,stop: int, step: int = 1):
    """
    >>> gen_range(0,10)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> gen_range(0,10,3)
    [0, 3, 6, 9]
    >>> gen_range(0,10,-1)
    []
    >>> gen_range(10,0)
    []
    >>> gen_range(10,0,-2)
    [10, 8, 6, 4, 2]
    >>> gen_range(-10,-3,2)
    [-10, -8, -6, -4]
    >>> gen_range(0.0,10)
    Traceback (most recent call last):
    TypeError: One of 'start', 'stop' or 'step' is not an integer
    >>> gen_range(0,10,0)
    Traceback (most recent call last):
    ValueError: 'step' has been assigned value 0 - imposible
    """

    if not isinstance(start,int) or not isinstance(stop,int) or not isinstance(step,int):
        raise TypeError("One of 'start', 'stop' or 'step' is not an integer")
    if step==0:
        raise ValueError("'step' has been assigned value 0 - imposible")
    if start<=stop and step<0 and start<0:
        return special_case(start,stop,step)
    if start<stop and step>0 or start>stop and step<0:
        return [start]+gen_range(start+step,stop,step)
    elif start>=stop or start<=stop and step<0 and start>=0:
        return []


if __name__=='__main__':
    import doctest
    doctest.testmod()