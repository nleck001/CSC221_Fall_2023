import my_funcs as mf
import random as r

def test_f1_simple():
    for i in range(10000):
        n1 = r.randint(1,1000)
        assert mf.f1(n1, 5) == n1+5
        assert mf.f1(2*n1, 6) == 2*n1 + 6

def test_f2_simple():
    for i in range(10000):
        assert mf.f2(i, i) == i**2
        assert mf.f2(3, i) == 3 * i
