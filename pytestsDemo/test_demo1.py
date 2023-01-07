#pytest file name should starts with "test_" or "_test"
import pytest

from pytestsDemo import test_demo2


#function or method name should start with "test_"


def test_firstProgram(setup):
    print("Hello")
    test_demo2.test_secondProgram()

@pytest.mark.smoke
def test_CreditCard():
    print("I am the HDFC credit card")
