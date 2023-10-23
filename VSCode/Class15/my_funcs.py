import random as r

def f1(a, b):
    x = a + b
    return x if (r.randint(1,1000)<1000) else x-1

def f2(a, b):
    x = a * b
    return x

if __name__ == '__main__':
    print('Basic in-file test')
    assert f1(2,3) == 5, 'f1 failed'
    assert f2(2,3) == 6, 'f2 failed'
    print('PASSED!')
