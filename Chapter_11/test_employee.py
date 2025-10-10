import pytest
from employee import Employee

@pytest.fixture
def test_employee():
    test_employee = Employee('citizen', 'kane', 80000)
    return test_employee

def test_give_default_raise(test_employee):
    #Does default raise work correctly
    test_employee.give_raise()
    assert test_employee.salary == 85000

def test_give_custom_raise(test_employee):
    #does custom raise amount work correctly
    test_employee.give_raise(20000)
    assert test_employee.salary == 100000