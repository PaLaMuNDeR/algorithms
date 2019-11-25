"""
Three Number Sum
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
The function should find all triplets in the array that sum up to the target sum and return a two-dimensional
array of all these triplets. The numbers in each triplet should be ordered in ascending order, and the triplets
themselves should be ordered in ascending order with respect to the numbers they hold. If no three numbers sum up to
the target sum, the function should return an empty array.
Sample input: [12, 3, 1, 2, -6, 5, -8, 6], 0 Sample output: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
"""

# # Time O(n) and Space O(n^2)
def threeNumberSum(array, targetSum):
    dict = {}
    answer = []
    for i in array:
        dict[i] = []

    for i in dict.keys():
        for j in dict.keys():
            if i != j:
                k = targetSum - i - j
                if k != i and k != j and k in dict.keys():
                    if j in dict[i] and k in dict[i] and i in dict[j] and k in dict[j] and i in dict[k] and j in dict[k]:
                        pass
                    else:
                        dict[i].append(j)
                        dict[i].append(k)
                        dict[j].append(i)
                        dict[j].append(k)
                        dict[k].append(i)
                        dict[k].append(j)

                        answer.append(sorted([i,j,k]))

    return sorted(answer)


# Time O(n^2) and Space O(n^2)
def threeNumberSum(array, targetSum):
    array.sort()
    answer = []
    for i in range(0, len(array)):
        current_sum = targetSum - array[i]
        # for left in range(i, len(array)):
        left = i+1
        right = len(array)-1

        while left < right:
            if array[left] + array[right] + array[i] == targetSum:
                answer.append([array[i], array[left], array[right]])
                left = left + 1
            elif array[left] + array[right] + array[i] < targetSum:
                left = left + 1
            elif array[left] + array[right] + array[i] > targetSum:
                right = right - 1

    return answer


print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))
print(threeNumberSum([1,2,3], 7))
print(threeNumberSum([12,3,1,2,-6,5,0,-8,-1,6,-5],0))
print(threeNumberSum([12,3,1,2,-6,5,-8,6],0))
print(threeNumberSum([1, 4, 45, 6, 10, 8],22))

