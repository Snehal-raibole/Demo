import pytest

@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixtureDemo1(self):
        print("I am test_fixtureDemo1")

    def test_fixtureDemo2(self):
        print("I am test_fixtureDemo2")


    def test_fixtureDemo3(self):
        print("I am test_fixtureDemo3")


    def test_fixtureDemo4(self):
        print("I am test_fixtureDemo4")
