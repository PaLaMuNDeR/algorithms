"""
Max Sum Increasing Subsequence
Given an non-empty array of integers, write a function that returns an array of length 2.
The first element in the output array should be an integer value representing the greatest sum that can be generated
from a strictly-increasing subsequence in the array. The second element should be an array of the numbers in that
subsequence. A subsequence is defined as a set of numbers that are not necessarily adjacent but that are in the same
order as they appear in the array. Assume that there will only be one increasing subsequence with the greatest sum.
Sample input: [10, 70, 20, 30, 50, 11, 30] Sample output: [110, [10, 20, 30, 50]]

"""

def maxSumIncreasingSubsequence(array):
    sums = [float("-inf") for i in range(len(array))]
    sequences = [None for i in range(len(array))]
    sums[0] = array[0]
    for i in range(len(array)):
        for j in range(0,i):
            if array[j] < array[i]:
                if sums[i] < array[i] + sums[j]:
                    sums[i] = array[i]+sums[j]
                    sequences[i] = j

            if array[i] > sums[i]:
                sums[i] = array[i]
                sequences[i] = None

    highest = float("-inf")
    index = 0
    for i in range(len(sums)):
        if sums[i] > highest:
            highest = sums[i]
            index = i
    answer = []
    while index is not None:
        answer.append(array[index])
        index = sequences[index]

    return [highest, answer[::-1]]

print(maxSumIncreasingSubsequence([8,12,2,3,15,5,7]))