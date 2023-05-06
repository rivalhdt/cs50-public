from working import convert
import pytest

def test():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test2():
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"

def test3():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test4():
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test5():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test6():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"

def test7():
    # to
    with pytest.raises(ValueError):
        convert("9 AM - 10 PM")

def tes8():
    # m 60
    with pytest.raises(ValueError):
        convert("9:80 AM to 10:100 PM")

def test9():
    # format inalid
    with pytest.raises(ValueError):
        convert("23:00 AM to 17:00 PM")

def test10():
    # explore
    with pytest.raises(ValueError):
        convert("2 to 1")