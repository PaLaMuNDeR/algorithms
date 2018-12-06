import timeit
import operator
""" Given a string, return the character that is most commonly used in the string.

Examples:

maxChar("abcccccccdef") -> "c"
maxChar("apple 12311111") -> "1"
 """


def maxChar(str):
    chars={}
    for i in str:
        chars[i] = chars[i] + 1 if i in chars.keys() else 1
    print chars
    return max(chars.iteritems(), key=operator.itemgetter(1))[0]



print(maxChar("abcdee"))
print(maxChar("abcccccccdef"))
print(maxChar("apple 12311111"))
# a_string = 'amanaplanacanalpanama' * 10
# print "Method 1 - Reccursion"
# print min(timeit.repeat(lambda: palindrome_recursive(a_string)))
#
# print "Method 2 - Reversed of a string"
# print min(timeit.repeat(lambda: palindrome_reverse(a_string)))

