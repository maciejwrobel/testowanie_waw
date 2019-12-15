# def dodawanie(x,y):
#     return x+y
#
# def test_add():
#     assert dodawanie(1,2) == 3, "failed"
#     assert dodawanie(3,-2) == 1, "failed"
#     assert dodawanie(1.5,2.5) == 4, "failed"
#
# test_add()
#
def product(x,y):
    return x*y

def test_product():
    assert product(1,1) == 1, "failed"
    assert product(2, -2) == -4, "failed"
    assert product(1.5, 2) == 3, "failed"

test_product()