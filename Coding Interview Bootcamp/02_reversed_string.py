import timeit

"For a given string - print out the reversed the string"


# === Solutions ===
def reverse_string(n):
    """
        Reverses a string by attaching the last character to a new string.
        Execution time for a longer string:
        12.7 sec.
    """
    k = ""
    for i in n:
        k = i + k
    return k


def reversed_of_string(n):
    """
        Reversing a string by using `reversed` and `join`
        Execution time for a longer string:
            5.3 sec.
    """
    return ''.join(reversed(n))


def reverse_slice(n):
    """
        Reversing a string with the Python slice's function
        Execution time for a longer string:
            5.3 sec.
    """
    return n[::-1]


# Measure the execution time with this snippet below
# a_string = 'amanaplanacanalpanama' * 10
# print "Method 1 - Reverse with empty string"
# print min(timeit.repeat(lambda: reverse_string(a_string)))
# print "Method 2 - Reversed of a string"
# print min(timeit.repeat(lambda: reversed_of_string(a_string)))
# print "Method 3 - slice"
# print min(timeit.repeat(lambda: reverse_slice(a_string)))

