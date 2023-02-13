def swap_elements(a,b):
    aux=a
    a=b
    b=aux
    return a,b


def is_sorted(elements:list,ascending:bool) -> bool:
    for i in range(len(elements)-1):
        if ascending==True and elements[i]>elements[i+1]:
            return False
        elif ascending==False and elements[i]<elements[i+1]:
            return False
    return True


def sort(elements: list, ascending: bool = True):
    length=len(elements)
    while is_sorted(elements,ascending)==False:
        index=0
        while index<length-1:
            if ascending==True and elements[index]>elements[index+1]:
                elements[index],elements[index+1]=swap_elements(elements[index],elements[index+1])
            elif ascending==False and elements[index]<elements[index+1]:
                elements[index+1],elements[index]=swap_elements(elements[index+1],elements[index])
            index+=1
        length-=1

