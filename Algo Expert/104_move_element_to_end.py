"""
Move Element To End
You are given an array of integers and an integer. Write a function that moves all instances of that integer in the
array to the end of the array. The function should perform this in place and does not need to maintain the order of the
other integers.
Sample input: [2, 1, 2, 2, 2, 3, 4, 2], 2 Sample output: [1, 3, 4, 2, 2, 2, 2, 2] (the numbers 1, 3, and 4 could be
ordered differently)

"""


# # Time: O(n) | Space: O(n)
# def moveElementToEnd(array, toMove):
#     """
#     Keep the values in new array
#     :param array:
#     :param toMove:
#     :return:
#     """
#     counter = 0
#     new_array = []
#     for i in array:
#         if i == toMove:
#             counter += 1
#         else:
#             new_array.append(i)
#     for i in range(counter):
#         new_array.append(toMove)
#     return new_array

# Time: O(n) | Space: O(1)
def moveElementToEnd(array, toMove):
    """
    Move two indeces that check the beginning and the end. Swap the values when needed until the indeces meet
    :param array:
    :param toMove:
    :return:
    """
    i = 0
    j = len(array) -1
    while i < j:
        if array[j] == toMove:
            j = j-1
        elif array[i] == toMove:
            c = array[i]
            array[i] = array[j]
            array[j] = c
            i += 1
        else:
            i += 1
    return array


print(moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2))