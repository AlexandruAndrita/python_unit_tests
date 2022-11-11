import math


def create_train_test_splits(data: list, train_size: float) -> tuple:
    if len(data)==0:
        return ([],[])

    train_size=math.floor(train_size*10)
    train_set=data[:train_size]
    test_set=data[train_size:len(data)]

    return (train_set,test_set)


