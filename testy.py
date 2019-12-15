import funkcje
import math
import pytest


def test_add():
    assert funkcje.dodawanie(1, 2) == 3
    assert funkcje.dodawanie(3, -2) == 1
    assert funkcje.dodawanie(1.5, 2.5) == 4


def test_product():
    assert funkcje.product(1, 1) == 1
    assert funkcje.product(2, -2) == -4
    assert funkcje.product(1.5, 2) == 3

def test_kwadrat():
    assert funkcje.kwadrat(1) == 1
    assert funkcje.kwadrat(0) == 0
    assert funkcje.kwadrat(-2) == 4

def test_is_palindrome():
    assert funkcje.is_palindrome("")
    assert funkcje.is_palindrome("Sedes")
    assert funkcje.is_palindrome("Kobyła ma mały BOK")

def test_circle_area():
    assert funkcje.circle_area(1) == math.pi
    assert funkcje.circle_area(0) == 0
    assert funkcje.circle_area(2.1) == math.pi * (2.1**2)


def test_values():
    with pytest.raises(ValueError):
        funkcje.circle_area(-2)

def test_type():
    with pytest.raises(TypeError):
        funkcje.circle_area("asdas")

test_add()
test_product()
test_kwadrat()
test_is_palindrome()
test_circle_area()