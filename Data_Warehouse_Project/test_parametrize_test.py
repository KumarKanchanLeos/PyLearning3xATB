import pytest

products=[(2,3,6),(3,3,9),(0,99,0),(-5,-5,25)]

@pytest.mark.parametrize('a,b,output',products)
def test_multiplication(a,b,output):
       assert a*b==output



