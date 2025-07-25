import pytest


@pytest.mark.order(1)
def test_order_1():
    print("test order 1")

@pytest.mark.skip("Under Development")
def test_order_2():
    print("test order 2")

@pytest.mark.order(2)
def test_order_3():
    print("test order 3")