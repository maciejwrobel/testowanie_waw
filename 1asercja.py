# def div(a,b):
#     return a/b
#
# # if div(10,5)==2:
# #     print("passed")
# # else:
# #     print("failed")
#
# # albo
#
# assert div(10,5) == 2, "Failed"
# print("passed")
# assert div(10,2) == 5, "Failed"
# print("passed")

# def kwadrat_sumy(a,b):
#     return (a+b)**2
#
# assert kwadrat_sumy(1,1) == 4 , "Failed"
# print("passed")
# assert kwadrat_sumy(2,2) == 16 , "Failed"
# print("passed")
# assert kwadrat_sumy(3,3) == 36 , "Failed"
# print("passed")

# asercje nie s lużą tylko do testowania !
# przykład:

# def div(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         print("nie można dzielić przez zero")
# # a jeszcze lepiej i krócej:
#
# def div(a,b):
#     assert b!=0, "Nie można dzielić przez zero"
#     return a/b
# div(5,0)

def konkatenacja(a,b):
    return a+b

assert konkatenacja("Ala ma ", "kota.") == "Ala ma kota.", "failed"
assert konkatenacja("Ola ma ", "psa.") == "Ola ma psa.", "failed"
assert konkatenacja("","") == "", "failed"

