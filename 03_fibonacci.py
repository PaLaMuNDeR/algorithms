
def fib(n):
    """ Finds the n-th Fibonaci number"""
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def print_fib_sequence(n):
    """
    Prints all the fibbonacci sequence up to n
    """
    for i in range(1, n+1):
        print fib(i)


print_fib_sequence(10)