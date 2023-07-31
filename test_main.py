from main import greet, inc

def test_greet():
    assert greet("Navid") == "Hello, Navid!"
    
def test_answer():
    assert inc(3) == 5