import timeit
"""
Write a program that prints the numbers from 1 to n. But for multiples of three print "Fizz" instead of the number
and for the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".
"""


# === Solution ===
def fizzbuzz(n):
    """ divisible by 3 - Fizz,
        divisible by 5 - Buzz,
        divisible by 15 - FizzBuzz
    """
    for i in range (1, n+1):
        if i % 15 == 0:
            print "FizzBuzz"
        elif i % 3 == 0:
            print "Fizz"
        elif i % 5 == 0:
            print "Buzz"
        else: print i

fizzbuzz(15)
