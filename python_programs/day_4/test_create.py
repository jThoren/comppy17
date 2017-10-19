import mycomplex

def test_create():
    z = mycomplex.MyComplex()
    assert z.re == 0.0
    assert z.im == 0.0

def test_create2():
    z = mycomplex.MyComplex(1.5,2.0)
    assert z.re == 1.5
    assert z.im == 2.0

def test_conjugate():
    z = mycomplex.MyComplex(1.0,1.0)
    z_c = z.conjugate()
    assert z.re == z_c.re
    assert z.im == -z_c.im

def test_add():
    z1 = mycomplex.MyComplex(1.0,1.0)
    z2 = mycomplex.MyComplex(0.5,0.7)
    z = z1 + z2
    assert z.re == 1.5
    assert z.im == 1.7

def test_add_complex_and_float():
    z1 = mycomplex.MyComplex(1.0,1.0)
    x = 2.0
    z = z1 + x
    assert z.re == 3.0
    assert z.im == 1.0

def test_add_float_and_complex():
    z1 = mycomplex.MyComplex(1.0,1.0)
    x = 2.0
    z = x + z1
    assert z.re == 3.0
    assert z.im == 1.0

def test_multiply():
    z1 = mycomplex.MyComplex(1.0,1.0)
    z2 = mycomplex.MyComplex(2.0,3.0)
    z = z1 * z2
    assert z.re == -1.0
    assert z.im == 5.0




