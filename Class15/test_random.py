import sample_functions as sf
import random as r

def test_test1_random():
    for i in range(300):
        x = r.randint(-900, 900)
        assert sf.test1(x) == x + 1


def test_test2_random():
    for i in range(300):
        x = r.randint(-900, 900)
        assert sf.test2(x) == x + 2
