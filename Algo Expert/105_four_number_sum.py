"""
Four Number Sum
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
The function should find all quadruplets in the array that sum up to the target sum and return a two-dimensional
array of all these quadruplets in no particular order. If no four numbers sum up to the target sum, the function should
return an empty array.
Sample input: [7, 6, 4, -1, 1, 2], 16 Sample output: [[7, 6, 4, -1], [7, 6, 1, 2]]

"""

def fourNumberSum(array, targetSum):
    array.sort()
    # left = 0
    # mid = 1
    # mid2 = 2
    # right = len(array)-1
    solution = []
    for left in range(len(array)-3):

        for mid in range(left+1,len(array)-2):

            mid2 = mid + 1
            right = len(array) - 1
            while mid2 < right:

                currentSum = array[left] + array[right] + array[mid] + array[mid2]
                print ("{}, L: {}. M1: {}. M2: {}. R: {}, sum: {}, {}".format(array, left, mid, mid2, right, currentSum,
                                                                              solution))
                if currentSum == targetSum:
                    sol = [array[left],array[mid],array[mid2],array[right]]
                    solution.append(sol)
                    mid2 += 1
                elif currentSum < targetSum:
                    mid2 += 1
                else:
                    right = right - 1
    return solution

# print(fourNumberSum([5,-5,-2,2,3,-3],0))
# print(fourNumberSum([7, 6, 4, -1, 1, 2], 16))
# print(fourNumberSum([-2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4))
#print(fourNumberSum([1,2,3,4,5,6,7], 10))

