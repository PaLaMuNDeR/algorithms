"""
Single Cycle Check
You are given an array of integers. Each integer represents a jump of its value in the array. For instance, the integer 2 represents a jump of 2 indices forward in the array; the integer -3 represents a jump of 3 indices backward in the array. If a jump spills past the array's bounds, it wraps over to the other side. For instance, a jump of -1 at index 0 brings us to the last index in the array. Similarly, a jump of 1 at the last index in the array brings us to index 0. Write a function that returns a boolean representing whether the jumps in the array form a single cycle. A single cycle occurs if, starting at any index in the array and following the jumps, every element is visited exactly once before landing back on the starting index.
Sample input: [2, 3, 1, -4, -4, 2] Sample output: True

"""

def hasSingleCycle(array):
    i = array[0]
    numVisited = 0
    while numVisited < len(array):
        if i >= len(array):
            i = i % len(array)
        elif i<0:
            i = len(array) + i
        else:
            if array[i] is None:
                break
            numVisited += 1
            print(i)
            value = array[i]
            array[i] = None
            i = i + value
    for i in array:
        if i is not None:
            return False
    return True