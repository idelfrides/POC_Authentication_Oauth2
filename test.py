
from os.path import dirname, realpath


def test_path():
    print('\n\n\n')
    x = realpath(__file__)
    print('\n REAL PATH \n', x)
    
    print('\n DIR NAME \n', dirname(x))

    print('\n\n\n')
    

if __name__ == '__main__':
    test_path()
    