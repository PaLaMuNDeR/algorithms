import timeit

""" Given a string, return true if the string is palindrome
 or false if it is not. Palindromes are strings that
 form the same world if it is reversed. *Do* include spaces
 and punctuation in determining if the string is a palindrome.

 Examples:
     palimdrome('abba') = True
     palindrome('abc')  = False
 """


def palindrome_recursive(str):
    """30 sec"""
    if len(str) == 0:
        return True
    else:
        if str[0] == str[-1]:
            palindrome_recursive(str[1:-1])
        else:
            return False


def palindrome_reverse(str):
    """0.5 sec"""
    reversed = str[::-1]
    return str == reversed


a_string = 'amanaplanacanalpanama' * 10
print "Method 1 - Reccursion"
print min(timeit.repeat(lambda: palindrome_recursive(a_string)))

print "Method 2 - Reversed of a string"
print min(timeit.repeat(lambda: palindrome_reverse(a_string)))

