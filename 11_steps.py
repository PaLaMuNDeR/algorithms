import timeit
import re

""" Write a function that accepts a positive number N.
 The function should console log a step shape with N levels 
 using the # character. 
 Make sure the step has spaces on the right hand side.

 Examples:
 steps(2):
 '# '
 '## '
 steps(3):
 '#  '
 '## '
 '###'
 steps(4):
 '#   ' 
 '##  '
 '### '
 '####'
 
 """


def steps(n):
    """Just iterating on the numbers in one for loop
    Time: 1.35 sec (with 123 steps)
    Time: 0.78 sec (with 10 steps)"""

    for i in range(0, n):
        # print ('#'*(i+1)+' '*(n-i+1))
        return ('#'*(i+1)+' '*(n-i+1))


def steps_with_inner_loop(n):
    """
    A solution wit double loop (outer and inner loop).
    hIterating on the rows and then on the columns.
    Add to the string and print.
    Time: 10 sec(with 123 steps)
    Time: 1.78 sec (with 10 steps)"""
    for row in range(0, n):
        stair = ''

        for column in range(0, n):
            if column <= row:
                stair += '#'
            else:
                stair += ' '

        # print stair
        return stair


def recursion_steps(n, row=0, stair=''):
    """A recursive solution
    Time: Maximum recursion depth exceeded (with 123 steps)
    Time: 33 sec (with 10 steps)"""
    if n == row:
        return
    elif n == len(stair):
        # print stair
        return recursion_steps(n, row+1)
    if len(stair) <= row:
        stair += '#'
    else:
        stair += ' '
    recursion_steps(n, row, stair)

    #
    # elif n == 1:
    #     print "#"
    #     return "#"
    # else:
    #     stra = "#" + str(recursion_steps(n-1))+"a"
    #     print stra
    #     return stra

# steps(4)
# steps_with_inner_loop(4)
# recursion_steps(4)

step_counter = 10

print "Method 1 - Single loop"
print min(timeit.repeat(lambda: steps(step_counter)))

print "Method 2 - Inner loop"
print min(timeit.repeat(lambda: steps_with_inner_loop(step_counter)))

print "Method 3 - Recursive solution"
print min(timeit.repeat(lambda: recursion_steps(step_counter)))
