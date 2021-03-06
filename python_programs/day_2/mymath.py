# TDD: test driven development
# Doc-string, the first string in a function
def mymax(x,y):
    """
    Returns the max of variables that have the operator > defined
    
    Input parameters: x,y, any type with > defined.
    
    >>> mymax(3,5)
    5
    """
    return listmax([x,y])

# Extending our max function, what if we want more than 2 numbers?
def listmax(l):
    """
    Returns the max of a list of variables that have the operator > defined
    
    Input parameters: a list containing any types with > defined between them.
    
    >>> mymax(3,5)
    5
    """
    # Safety for the case where l is empty
    try:
        lmax = l[0]
    except IndexError:
        return None
    # Find the largest element of l
    for i in l:
        if i > lmax:
            lmax = i
    return lmax

if __name__ == "__main__":
    import doctest
    doctest.testmod()
