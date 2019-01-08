import timeit
import re

""" Write a function that returns the number of vowels used in a
 string. Vowels are characters 'a', 'e', 'i', 'o', 'u'
 
 Examples:
 vowels('Hi There!') -> 3
 vowels('Why do you ask?') -> 4
 vowels('Why?') -> 0
  
 """


def vowels(text):
    """Just iterating on the letters and comparing them with the vowels
    Time:17.5 sec
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    counter = 0
    text = text.lower()
    for i in text:
        if i in vowels:
            counter += 1

    return counter


def vowels_re(text):
    """Regular Expression
    Time: 17.97 sec
    """
    matches = re.findall('a|i|e|o|u', text)
    return len(matches) if matches else 0

#
# print(vowels('Hi There!'))
# print(vowels('Why do you ask?'))
# print(vowels('Why?'))
#
# print(vowels_array('Hi There!'))
# print(vowels_array('Why do you ask?'))
# print(vowels_array('Why?'))

a_string = 'amanaplanacanalpanama' * 10

print "Method 1 - Array"
print min(timeit.repeat(lambda: vowels(a_string)))

print "Method 2 - Regular Expression"
print min(timeit.repeat(lambda: vowels_re(a_string)))
