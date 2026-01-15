from broken_module import is_even

def test_even_number():
    assert is_even(4)

def test_odd_number():
    assert not is_even(5)
