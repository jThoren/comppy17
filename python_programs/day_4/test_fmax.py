import fmax
import unittest.mock as mock

def test_filemax():
    # We would prefer not to interact with the file system when testing,
    # so preferably we would like to have a fake file instead of creating a file
    with open('test.dat','w') as f:
        f.write("""
        1
        3
        5
        4
        """)
    with open('test.dat','r') as f:
        fm = fmax.filemax(f)
    assert fm == 5

# Here we make use of the unittest module mock, it lets us
# do this test without touching the file system
@mock.patch('fmax.open')
def test_filemaxname(mock_open):
    mock_open.return_value = ["1","5","3"]
    fm = fmax.filemaxname('not_a_file.dat')
    assert fm == 5
