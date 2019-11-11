import timeit

""" Write a function that accepts a string. The function should 
capitalize the first letter of each word in the string then 
return the capitalized string.

 Examples:
     capitalize('a short sentence') -> 'A Short Sentence'
     capitalize('a lazy fox') -> 'A Lazy Fox'
     capitalize('look, it is working!') -> 'Look, It Is Working!'
 """


def capitalize_move_index(str):
    """
        Find a space, set index var to it and update the next char
        Time: 16 sec.
    """
    index = 0
    str = str[index].upper() + str[index + 1:]
    index = index + str[index + 1:].find(' ') + 1

    while index < len(str):
        str = str[0:index] + ' ' + str[index+1].upper() + str[index+2:]
        next_space = str[index+1:].find(' ')
        if not next_space == -1:
            index = index + next_space + 1
        else: break

    return str


def capitalize_with_array(str):
    """
        Split to array of words.
        Convert the first letter of each to capital.
        Join all the words
        Time: 9 sec.
    """
    index = 0
    words = []
    for word in str.split(' '):
        words.append(word[0].upper() + word[1:])

    return (' ').join(words)


def capitalize_after_space(str):
    """
        Before you find a space, make the next character UpperCase
        Time: 32 sec.
    """
    result = str[0].upper()

    for i in range(1, len(str)):
        if str[i-1] == ' ':
            result += str[i].upper()
        else:
            result += str[i]

    return result



# print(capitalize_after_space('a short sentence') )
# print(capitalize_after_space('a lazy fox'))
# print(capitalize_after_space('look, it is working!'))


a_string = 'amanaplana canal panama' * 10

print "Method 1 - Find a space, set index var to it and capitalize after"
print min(timeit.repeat(lambda: capitalize_move_index(a_string)))

print "Method 2 - Split to array of words"
print min(timeit.repeat(lambda: capitalize_with_array(a_string)))

print "Method 3 - Capitalize everything after space"
print min(timeit.repeat(lambda: capitalize_after_space(a_string)))


