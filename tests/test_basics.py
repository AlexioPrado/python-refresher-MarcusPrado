from basics import calculate_discount

def test_member_discount():
    assert calculate_discount(100, True) == 90

def test_non_member():
    assert calculate_discount(100, False) == 100

def test_negative_price():
    try:
        calculate_discount(-50, True)
        assert False
    except ValueError:
        assert True
