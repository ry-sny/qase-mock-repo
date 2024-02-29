import random
import time

import pytest


@pytest.mark.parametrize("number", [1, 2, 3, 4, 5])
def test_params(number):
    print("test")
    assert number % 3 != 0


def test_random_sleep():
    time.sleep(random.randrange(6))



