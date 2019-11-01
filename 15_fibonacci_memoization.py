import timeit
import functools


def fib(n):
    """
        Prints the first n Fibonacci numbers recursively
        Time: 11 sec
    """
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


print ("Method 1 - Recursive")
# print (min(timeit.repeat(lambda: fib(10))))


def fib_iterative(n):
    """
        Iterative solution for Fibonacci's sequence
        Time: 2.6 sec
    """
    result = [0,1]

    for i in range(2,n+1):
        a = result[i-1]
        b = result[i-2]

        result.append(a+b)

    return result[n]


print ("Method 2 - Iterative")
print (min(timeit.repeat(lambda: fib_iterative(10))))


def memoize(func):
    """
        Memoization function - we cache the outcome of
        the many calls that fib makes to itself.
        Time: 0.76 sec
    """
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func


fib = memoize(fib)

print ("Method 3 - Memoization")
print (min(timeit.repeat(lambda: memoize(fib(10)))))


@functools.lru_cache(maxsize=128)
def fibonacci(n):
    """
        Using the memoization function in Python3
        Time 0.63
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print ("Method 4 - Memoization with functools cache")
print (min(timeit.repeat(lambda: memoize(fibonacci(10)))))
