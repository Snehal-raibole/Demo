import random

import pytest

names = ["Vinay", "Theo", "Akshay"]


#method name should make sense in order to execute it seprately
#-v more info like metadata
#-k method name execution like recursive calling for method/ function
#-s log in output
#pytest to execute program on cmd "python -m pytest "test_demo1.py" -s -v
#cms path shoud be current dir of *.py file
#creating a set of TC with mark "@pytest.mark.smoke" smoke is the group name of TC, mark is the inbuild function
#to use it just add this statment before the method
#python -m pytest -m smoke -s -v excution cmd
#@pytest.mark.skip "skip" inbuild mark to skip a TC in suite
#@pytest.mark.xfail, this script will execute but report doesnot contails its result

@pytest.mark.smoke
@pytest.mark.skip
def test_secondProgram():
    print("Snehal")
    print(random.choice(names))

@pytest.mark.xfail
def test_CreditCardSBI():
    print("I am  the SBI credit card")
