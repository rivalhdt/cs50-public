from twttr import shorten

def test_shorten():
    assert shorten("aldy") == "ldy"
    assert shorten("david") == "dvd"

def test_without_cap():
    assert shorten("DaVid") == "DVd"

def test_all_cap():
    assert shorten("DAVID") == "DVD"

def test_number():
    assert shorten("David10") == "Dvd10"

def test_punctuation():
    assert shorten("David?") == "Dvd?"