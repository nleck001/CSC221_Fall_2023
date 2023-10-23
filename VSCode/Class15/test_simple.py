import my_funcs as mf

def test_f1_simple():
    assert mf.f1(3, 5) == 8
    assert mf.f1(3, 6) == 9

def test_f2_simple():
    assert mf.f2(3,5) == 15
    assert mf.f2(3, 11) == 33

