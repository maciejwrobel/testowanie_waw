import math

def dodawanie(x,y):
    return x+y

def product(x,y):
    return x*y

def kwadrat(x):
    return x**2

def is_palindrome(str1):
    return str1.lower().replace(" ","") == str1[::-1].lower().replace(" ","")

def circle_area(r):
    if r<0:
        raise ValueError("the radius cannot be nageative")
    if type(r) not in [int, float]:
        raise TypeError("the radius be a non-negative real number")
    return math.pi *r**2