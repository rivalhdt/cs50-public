from fuel import gauge, convert
import pytest

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(75) == "75%"

def test_convert():
    assert convert("3/4") == 75
    assert convert("2/4") == 50
    assert convert("0/4") == 0
    assert convert("4/4") == 100

def test_zero():
    with pytest.raises(ZeroDivisionError):
        assert convert("4/0")

def test_string():
    with pytest.raises(ValueError):
        assert convert("cat")

def test_string():
    with pytest.raises(ValueError):
        assert convert("4/3")
