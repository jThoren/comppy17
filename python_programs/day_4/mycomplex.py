"""
Module for complex numbers
"""

class MyComplex:
    # Real and imaginary parts are optional arguments
    def __init__(self,re=0.0,im=0.0):
        self.re = re
        self.im = im

    # We could make this function change self, or create a new
    # object that is the conjugate, we choose for it to create
    # a new object and return it
    def conjugate(self):
        return MyComplex(self.re,-self.im)

    # This is defined to be the binary operator +
    # have to define behaviour if we try to add a float
    # to the complex number
    def __add__(self,other):
        if type(other) == float:
            return MyComplex(self.re + other,self.im)
        return MyComplex(self.re + other.re,self.im + other.im)
    
    # To deal with the case of adding a complex number to a float
    # x + z, we have the reserved name __radd__
    def __radd__(self,other):
        return MyComplex(self.re + other,self.im)
    
    def __mul__(self,other):
        re = self.re * other.re - self.im * other.im
        im = self.re * other.im + self.im * other.re
        return MyComplex(re,im)
