import sys

# Example of making our own exception
class NonPositiveInputError(Exception):
    pass

def square(x):
    return x*x

def square_pos(x):
    import pdb; pdb.set_trace()
    if x <= 0:
        raise NonPositiveInputError
    return x*x

if __name__ == '__main__':
    try:
        arg = float(sys.argv[1])
        res = square_pos(arg)
    except IndexError:
        print("Usage: {} number".format(sys.argv[0]))
        sys.exit()
    except ValueError:
        print("{}: {} is not a number".format(sys.argv[0],sys.argv[1]))
        sys.exit()
    except NonPositiveInputError:
        print("{}: {} is not a positive number".format(sys.argv[0],sys.argv[1]))
        sys.exit()
    print(res)
    
