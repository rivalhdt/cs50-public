from bank import value

def test():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("halo") == 20
    assert value("HALO") == 20
    assert value("what's up?") == 100
    assert value("What's Up?") == 100