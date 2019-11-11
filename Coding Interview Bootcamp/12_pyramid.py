import timeit
from math import floor

""" Write a function that accepts a positive number N.
 The function should console log a pyramid shape
 with N levels using the # character.  
 Make sure the step has spaces on the right and left hand side.

 Examples:
 pyramid(1):
 '#'
 pyramid(2):
 ' # '
 '###'
 steps(3):
 '  #  '
 ' ### '
 '#####'
 steps(4):
 '   #   ' 
 '  ###  '
 ' ##### '
 '#######'
 
 """


def pyramid(n):
    """Just iterating on the numbers in one for loop
    Time:  5.21 sec (with 10 steps)"""
    answer = ''
    for i in range(0, n):
        answer += '_'*(n-i-1)+'#'*(2*i+1)+'_'*(n-i-1)+'\n'

    # print answer
    return answer


def pyramid_with_inner_loop(n):
    """
    A solution wit double loop (outer and inner loop).
    hIterating on the rows and then on the columns.
    Add to the string and print.
    Time:  43.40 sec (with 10 steps)"""
    answer = ''
    for row in range(0, n):
        stair = ''
        midpoint = floor((2 * n - 1) / 2)

        for column in range(0, (2*n-1)):
            if midpoint - row <= column and midpoint + row >= column:
                stair += '#'
            else:
                stair += '_'

        answer += stair + '\n'

    # print answer
    return answer


def recursion_pyramid(n, row=0, stair=''):
    """A recursive solution
    Time: Maximum recursion depth exceeded (with 123 steps)
    Time: 122 sec (with 10 steps)"""
    if n == row:
        return
    elif 2*n-1 == len(stair):
        # print stair
        return recursion_pyramid(n, row+1)

    midpoint = floor((2 * n - 1) / 2)
    if len(stair) >= midpoint - row and midpoint + row >= len(stair):
        add = '#'
    else:
        add = '_'

    recursion_pyramid(n, row, stair+add)

# pyramid(4)
# pyramid_with_inner_loop(4)
# recursion_pyramid(4)

step_counter = 10

print "Method 1 - Single loop"
print min(timeit.repeat(lambda: pyramid(step_counter)))

print "Method 2 - Inner loop"
print min(timeit.repeat(lambda: pyramid_with_inner_loop(step_counter)))

print "Method 3 - Recursive solution"
print min(timeit.repeat(lambda: recursion_pyramid(step_counter)))
