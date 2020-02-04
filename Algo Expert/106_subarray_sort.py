"""
Subarray Sort
Write a function that takes in an array of integers of length at least 2. The function should return an array of the
 starting and ending indices of the smallest subarray in the input array that needs to be sorted in place in order for
  the entire input array to be sorted.  If the input array is already sorted, the function should return [-1, -1].
Sample input: [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19] Sample output: [3, 9]

"""
# check the misplaced elements, take the min and max from them
# and look at what positions they should be in the initial array
def subarraySort(array):
    answer = [-1,-1]
    min_misplaced = float("inf")
    max_misplaced = float("-inf")
    for i in range(len(array)-1):
        if array[i] <= array[i+1]:
            pass
        else:
            min_misplaced = min(array[i+1], min_misplaced)
            min_misplaced = min(array[i], min_misplaced)
            max_misplaced = max(array[i+1], max_misplaced)
            max_misplaced = max(array[i], max_misplaced)

    print("min: {}, max: {}".format(min_misplaced, max_misplaced))
    for i in range(len(array)):
        if array[i] > min_misplaced:
            answer[0] = i
            break
    for i in range(len(array)-1,0,-1):
        if array[i] < max_misplaced:
            answer[1] = i
            break

    return answer


# print(subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))
# print(subarraySort([1, 2]))
print(subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 13, 14, 16, 18, 19]))
