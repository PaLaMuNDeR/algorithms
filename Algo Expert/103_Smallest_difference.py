"""
Smallest Difference
Write a function that takes in two non-empty arrays of integers. The function should find the pair of numbers
(one from the first array, one from the second array) whose absolute difference is closest to zero.
The function should return an array containing these two numbers, with the number from the first array in the first
position. Assume that there will only be one pair of numbers with the smallest difference.
Sample input: [-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17] Sample output: [28, 26]

"""

# Time O(n^2) | Space (1)
# def smallestDifference(arrayOne, arrayTwo):
#     """
#     Trivial double for-loop
#     :param arrayOne:
#     :param arrayTwo:
#     :return:
#     """
#     best_diff = abs(arrayOne[0] - arrayTwo[0])
#     for i in arrayOne:
#         for j in arrayTwo:
#             diff = abs(i-j)
#             if diff < best_diff:
#                 best_diff = diff
#                 current_elem1 = i
#                 current_elem2 = j
#
#     return [current_elem1, current_elem2]


# Time O(n*log(n) + m*log(m)) | Space (1)
def smallestDifference(arrayOne, arrayTwo):
    """
    Sort out the array and look for the indeces
    """
    arrayOne.sort()
    arrayTwo.sort()
    best_diff = abs(arrayOne[0] - arrayTwo[0])
    current_elem1 = arrayOne[0]
    current_elem2 = arrayTwo[0]
    indexOne = indexTwo = 0
    while indexOne < len(arrayOne) and indexTwo < len(arrayTwo):
        if arrayOne[indexOne] == arrayTwo[indexTwo]:
            return [arrayOne[indexOne], arrayTwo[indexTwo]]
        else:
            if abs(arrayOne[indexOne]-arrayTwo[indexTwo]) < best_diff:
                best_diff = abs(arrayOne[indexOne]-arrayTwo[indexTwo])
                current_elem1 = arrayOne[indexOne]
                current_elem2 = arrayTwo[indexTwo]

            if arrayOne[indexOne] < arrayTwo[indexTwo]:
                indexOne += 1
            elif arrayOne[indexOne] > arrayTwo[indexTwo]:
                indexTwo += 1

    return [current_elem1, current_elem2]


print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))