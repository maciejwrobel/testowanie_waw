from funkcje import product, dodawanie, kwadrat

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

test_add()
test_product()
test_kwadrat()