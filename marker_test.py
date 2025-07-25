#test case prioritize
#test case grouping
import pytest


@pytest.mark.high
def test_critical_function_1():
    print("Critical function 1")
    pass

@pytest.mark.high
def test_critical_function_2():
    print("Critical function 2")
    pass

@pytest.mark.high
def test_critical_function_3():
    print("Critical function 3")
    pass

@pytest.mark.medium
def test_normal_function_1():
    print("Normal function 1")
    pass

@pytest.mark.medium
def test_normal_function_2():
    print("Normal function 2")
    pass

@pytest.mark.low
def test_unimportant_function():
    print("Unimportant function 1")
    pass

