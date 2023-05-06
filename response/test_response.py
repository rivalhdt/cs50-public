from response import valid

def test():
    assert valid("malan@harvard.edu") == "Valid"
    assert valid("aldy@gmail.com") == "Valid"
    assert valid("malan@@@harvard.edu") == "Invalid"
    assert valid("malan@harvard..com") == "Invalid"
    assert valid("malan") == "Invalid"
    assert valid("malan at harvard dot edu") == "Invalid"
    assert valid("aldy") == "Invalid"
    assert valid("aldy.com") == "Invalid"