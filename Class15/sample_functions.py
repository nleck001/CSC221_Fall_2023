import random as r

def test1(x):
    c = x+1 if(r.randint(1,1000) < 1000) else x+2
    return c


def test2(y):
    c = y + 2
    return c
