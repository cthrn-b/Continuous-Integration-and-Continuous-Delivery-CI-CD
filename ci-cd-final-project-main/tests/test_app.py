from service import app

def test_add():
    assert app.add(3, 2) == 5

def test_subtract():
    assert app.subtract(5, 3) == 2
