import timeit
import re

""" Check to see if two provided strings are anagrams of each other.
One string is an anagram of another if it uses the same characters
in the same quantity. Only consider chars, not spaces or punctuation
Consider capital letters to be the same as lower case

 Examples:
     anagrams('rail safety', 'fairy tales') = True
     anagrams('RAIL! SAFETY!', 'fairy tales') = True
     anagrams('Hi there', 'Bye there') = False
 """


def anagrams(str1, str2):
    """
        Use Regular Expressions and store the two arrays in a dictionary.
        After that compare the dictionaries
        Time: 152 sec.
    """
    str1 = re.sub(r'[\s\W]', "", str1).lower()
    str2 = re.sub(r'[\s\W]', "", str2).lower()
    chars1 = {}
    chars2 = {}

    for i in str1:
        chars1[i] = chars1[i] + 1 if i in chars1.keys() else 1

    for j in str2:
        chars2[j] = chars2[j] + 1 if j in chars2.keys() else 1

    return chars1 == chars2


def anagrams_sort(str1, str2):
    """
        Use Regular Expressions and sort them
        Time: 55 sec.
    """
    str1 = sorted(re.sub(r'[\s\W]', "", str1).lower())
    str2 = sorted(re.sub(r'[\s\W]', "", str2).lower())

    return str1 == str2

#
# print(anagrams_sort('rail safety', 'fairy tales') )
# print(anagrams_sort('RAIL! SAFETY!', 'fairy tales'))
# print(anagrams_sort('Hi there', 'Bye there'))


a_string = 'amanaplanacanalpanama' * 10
a_string2 = 'aaaaaaaaaacllmmnnnnpp' * 10

print "Method 1 - Reccursion"
print min(timeit.repeat(lambda: anagrams(a_string, a_string2)))

print "Method 2 - Reversed of a string"
print min(timeit.repeat(lambda: anagrams_sort(a_string, a_string2)))

