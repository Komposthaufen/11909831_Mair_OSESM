
from Mair_OSESM_1HUE import is_prime
from Mair_OSESM_1HUE import is_even
from Mair_OSESM_1HUE import is_odd

def test_is_prime():
    assert not is_prime(3)
    assert not is_prime(7)
    assert not is_prime(4)


def test_is_even():
    assert not is_even(3)
    assert not is_even(4)
    assert not is_even(12)


def test_is_odd():
    assert not is_odd(3)
    assert not is_odd(5)
    assert not is_odd(12)