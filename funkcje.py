def dodawanie(x,y):
    return x+y

def product(x,y):
    return x*y

def kwadrat(x):
    return x**2

def is_palindrome(str1):
    return str1.lower().replace(" ","") == str1[::-1].lower().replace(" ","")