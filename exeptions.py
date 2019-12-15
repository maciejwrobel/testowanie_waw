from math import pi

# def circle_area(r):
#     if type(r) not in [int, float]:
#         print("podales nieprawidlowy typ, podaj liczbę")
#     elif r<0:
#         print("kolo o takim promieniu nie istnieje")
#     else:
#         return pi*r**2
#     return "error"
#
# print(circle_area(1))
# print(circle_area(0))
# print(circle_area(-1))
# print(circle_area(2+5j))
# print(circle_area(True))
# print(circle_area("asd"))

def circle_area(r):
    if r<0:
        raise Exception("promien nie moze byc ujemny")
    try:
        return pi*r**2
    except:
        return "coś poszło nie tak"

print(circle_area(0))
print(circle_area(-1))
print(circle_area(2+5j))
print(circle_area(True))
print(circle_area("asd"))