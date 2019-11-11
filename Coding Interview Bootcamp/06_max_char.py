import timeit
import operator
""" Given a string, return the character that is most commonly used in the string.

Examples:

maxChar("abcccccccdef") -> "c"
maxChar("apple 12311111") -> "1"
 """

# === Solution ===
def maxChar(str):
    """
    Store the characters in a dictionary.
    Then we use the operator library to return the key of the highest value of the dictionary.
    :param str: the string
    :return: the most repeated value
    """
    chars={}
    for i in str:
        chars[i] = chars[i] + 1 if i in chars.keys() else 1
    return max(chars.iteritems(), key=operator.itemgetter(1))[0]


# print(maxChar("abcdee"))
# print(maxChar("abcccccccdef"))
# print(maxChar("apple 12311111"))

assert maxChar("abcdee") == "e"
assert maxChar("abcccccccdef") == "c"
assert maxChar("apple 12311111") == "1"