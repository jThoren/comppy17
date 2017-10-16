# Defines a function, called mymax, taking the arguments x and y
def mymax(x, y):
    # We need the indentation here in python, it isn't
    # purely for readability
    if x > y:
        return x
    else:
        return y
# If return is left empty the default value is used, which is None

# Testing the function
i = 1
j = 2

if __name__ == "__main__":
    # The following looks like a tuple, at least in python 2.7
    print("The maximum of ",i," and ",j," is ", mymax(1,2))
    
    # C-like syntax of getting the output as a single string
    print("The maximum of %d and %d is %d" % (i, j, mymax(i,j)) )
    
    # Another way (python-like?)
    print("The maximum of {} and {} is {}".format(i,j,mymax(i,j)))
    
    # What if the number of args and brackets doesn't match?
    # The following is fine
    print("The maximum of {} and {} is".format(i,j,mymax(i,j)))
    # The following isn't, as it tries to access the 4th element of the tuple
    #print("The maximum of {} and {} is {} and not {}".format(i,j,mymax(i,j)))
    
    # The following requires python 3.6
    #print(f"The maximum of {i} and {j} is {mymax(i,j)}")


# Extending our max function, what if we want more than 2 numbers?
def listmax(l):
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

print(__name__)

if __name__ == "__main__":
    import sys
    print(sys.argv)
    myList = []
    for arg in sys.argv[1:]:
        myList.append(int(arg))
    print(myList)
    mySecondList = [int(arg) for arg in sys.argv[1:]]
    print(mySecondList)
    print(listmax(myList))
    
