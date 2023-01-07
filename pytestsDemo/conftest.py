import pytest


# to generlize fixture for multiple scripts conftest is used
# fixture are use to execute some funtion multiple time


@pytest.fixture(scope="class")
def setup():
    print("I will execute first")
    yield
    print("i will be excuted last")


@pytest.fixture()
def dataload():
    #print("Im the dataLoad method")
    return ["Snehal", "Raibole", "raibole@gmail.com"]

@pytest.fixture(params=[("Chrome", "Snehal", "Raibole"), ("IE", "Akshay", "Dhiware"), ("Firefox", "Theo")])
def crossBrowser(request):
    return request.param

for i in dataload:
    print(i)

