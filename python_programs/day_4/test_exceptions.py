import exceptions_example as ee


def test_square():
    x = 2.0
    y = -3.0
    assert ee.square(x) == 4.0
    assert ee.square(y) == 9.0
