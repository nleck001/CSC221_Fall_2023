import sample_functions as sf


def test_test1_basic():
    for i in range(30):
        assert sf.test1(i) == i + 1

def test_test1_basic_high():
    for i in range(2000, 2100):
        assert sf.test1(i) == i + 1

def test_test2_basic():
    for i in range(30):
        assert sf.test2(i) == i + 2
