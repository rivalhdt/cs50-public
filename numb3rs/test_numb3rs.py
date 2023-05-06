from numb3rs import validate

def test_valid():
    assert validate("255") == False

def first_byte():
    with pytest.raises(True):
        assert validate("1.555.555.555")