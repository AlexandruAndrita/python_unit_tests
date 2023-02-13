def clip(*values, min_=0, max_=1) -> list:
    if len(values)==0:
        return []

    new_list=[]
    for i in values:
        if i<min_:
            new_list.append(min_)
        elif i>max_:
            new_list.append(max_)
        else:
            new_list.append(i)

    return new_list