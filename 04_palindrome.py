import timeit

""" Given a string, return true if the string is palindrome
 or false if it is not. Palindromes are strings that
 form the same world if it is reversed. *Do* include spaces
 and punctuation in determining if the string is a palindrome.

 Examples:
     palimdrome('abba') = True
     palindrome('abc')  = False
 """


# ===Solutions===
def palindrome_recursive(str):
    """
    Trivial solution where we compare the first and last character.
    Then, we remove them from the string and call the function recursively again.

    Average runtime: 30 sec.
    """
    if len(str) == 0:
        return True
    else:
        if str[0] == str[-1]:
            palindrome_recursive(str[1:-1])
        else:
            return False


def palindrome_reverse(str):
    """
    Using the reversed string function of Python, we can just compare if the original string is the same as the reversed.
    Average time: 0.5 sec
    """
    reversed = str[::-1]
    return str == reversed


a_string = 'amanaplanacanalpanama' * 10
print "Method 1 - Reccursion"
print min(timeit.repeat(lambda: palindrome_recursive(a_string)))

print "Method 2 - Reversed of a string"
print min(timeit.repeat(lambda: palindrome_reverse(a_string)))

