from plates import is_valid

def test_alpha_number():
    assert is_valid("CS50") == True

def test_zero_first_num():
    assert is_valid("CS05") == False

def test_alpha_behind_number():
    assert is_valid("CS50P") == False

def test_punctuation():
    assert is_valid("PI3.14") == False

def test_one_len():
    assert is_valid("H") == False

def test_beginning():
    assert is_valid("23ADY") == False
    assert is_valid("ALDY") == True
    assert is_valid("2342") == False

def test_more_6_len():
    assert is_valid("OUTATIME") == False