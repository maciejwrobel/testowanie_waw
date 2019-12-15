from funkcje import product, dodawanie, kwadrat, is_palindrome

def test_add():
    assert dodawanie(1, 2) == 3
    assert dodawanie(3, -2) == 1
    assert dodawanie(1.5, 2.5) == 4


def test_product():
    assert product(1, 1) == 1
    assert product(2, -2) == -4
    assert product(1.5, 2) == 3

def test_kwadrat():
    assert kwadrat(1) == 1
    assert kwadrat(0) == 0
    assert kwadrat(-2) == 4

def test_is_palindrome():
    assert is_palindrome("")
    assert is_palindrome("Sedes")
    assert is_palindrome("Kobyła ma mały BOK")

test_add()
test_product()
test_kwadrat()
test_is_palindrome()