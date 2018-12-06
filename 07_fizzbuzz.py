import timeit

def fizzbuzz(n):
    """ divisible by 3 - Fizz,
        divisible by 5 - Buzz,
        divisible by 15 - FizzBuzz
    """
    for i in range (1, n):
        if i % 15 == 0:
            print "FizzBuzz"
        elif i % 3 == 0:
            print "Fizz"
        elif i % 5 == 0:
            print "Buzz"
        else: print i


def fib(n):
    """ Prints the first n Fibonaci numbers"""
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def print_fib(n):
    for i in range(1, n+1):
        print fib(i)


def reverse_string(n):
    """ Reverses a string """
    k = ""
    for i in n:
        k = i + k

    return k


def reversed_of_string(n):
    return ''.join(reversed(n))


def reverse_slice(n):
    return n[::-1]


#
# a_string = 'amanaplanacanalpanama' * 10
# print "Method 1 - Reverse with empty string"
# print min(timeit.repeat(lambda: reverse_string(a_string)))
# print "Method 2 - Reversed of a string"
# print min(timeit.repeat(lambda: reversed_of_string(a_string)))
# print "Method 3 - slice"
# print min(timeit.repeat(lambda: reverse_slice(a_string)))


