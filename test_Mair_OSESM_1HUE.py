
from Mair_OSESM_1HUE import is_prime
from Mair_OSESM_1HUE import is_even
from Mair_OSESM_1HUE import is_odd


def test_is_prime():
    assert is_prime(3) == True
    assert is_prime(7) == True
    assert is_prime(4) == False


def test_is_even():
    assert is_even(3) == False
    assert is_even(4) == True
    assert is_even(12) == True


def test_is_odd():
    assert is_odd(3) == True
    assert is_odd(5) == True
    assert is_odd(12) == False