import timeit

""" Given an int. return an int that is the reverse

Examples:
reverseInt(15) -> 51
reverseInt(189) -> 981
reverseInt(500) -> 5
reverseInt(-15) -> -51
reverseInt(-90) -> -9

 """

# ===Solution
def reverse_int(i):
    """
    We take the integer and convert it to string.
    Check if the first symbol is '-', then we reverse the string.
    In the end, we return it as an integer
    """
    string_of_i = str(i)
    if string_of_i[0] == '-':
        reverse = '-'
        string_of_i = string_of_i[1:]
    else:
        reverse = ''
    reverse = reverse + string_of_i[::-1]

    return int(reverse)

# print(reverse_int(15))
# print(reverse_int(189))
# print(reverse_int(500))
# print(reverse_int(-15))
# print(reverse_int(-90))
# print(reverse_int(-900))
# print(reverse_int(-901))
assert reverse_int(15) == 51
assert reverse_int(189) == 981
assert reverse_int(500) == 5
assert reverse_int(-15) == -51
assert reverse_int(-900) == -9
assert reverse_int(-901) == -109
