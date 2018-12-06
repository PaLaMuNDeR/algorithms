import timeit

""" Given an int. return an int that is the reverse

Examples:
reverseInt(15) -> 51
reverseInt(189) -> 981
reverseInt(500) -> 5
reverseInt(-15) -> -51
reverseInt(-90) -> -9

 """


def reverse_int(i):
    string_of_i = str(i)
    if string_of_i[0] == '-':
        reverse = '-'
        string_of_i = string_of_i[1:]
    else:
        reverse = ''
    reverse = reverse + string_of_i[::-1]

    return int(reverse)


print(reverse_int(15))
print(reverse_int(189))
print(reverse_int(500))
print(reverse_int(-15))
print(reverse_int(-90))
print(reverse_int(-900))
print(reverse_int(-901))

# a_string = 'amanaplanacanalpanama' * 10
# print "Method 1 - Reccursion"
# print min(timeit.repeat(lambda: palindrome_recursive(a_string)))
#
# print "Method 2 - Reversed of a string"
# print min(timeit.repeat(lambda: palindrome_reverse(a_string)))

