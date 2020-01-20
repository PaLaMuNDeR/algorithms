"""
Kadane's Algorithm
Write a function that takes in a non-empty array of integers and returns the maximum sum that can be obtained by summing
up all the numbers in a non-empty subarray of the input array. A subarray must only contain adjacent numbers.
Sample input: [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4] Sample output: 19 ([1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1])

"""

def kadanesAlgorithm(array):
    if len(array) == 1:
        return array[0]

    new_highest_sum = highest_sum = array[0]
    new_starting_index = 0
    currentIndex = previousIndex = array[0]

    for i in range(1,len(array)):
        if previousIndex > 0:
            currentIndex = array[i] + previousIndex
            if currentIndex > new_highest_sum:
                new_highest_sum = currentIndex
                ending_index = i
            if new_highest_sum > highest_sum:
                highest_sum = new_highest_sum
                starting_index = new_starting_index
        else:
            if array[i] > previousIndex:
                new_starting_index = i
                new_highest_sum = array[i]
                currentIndex = array[i]
                if new_highest_sum > highest_sum:
                    highest_sum = new_highest_sum
                    starting_index = new_starting_index

        # print(previousIndex)
        previousIndex = currentIndex

    return highest_sum

print(kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))
print(kadanesAlgorithm([1,2,3,4,5,6,-20,7,8,9,10]))
print(kadanesAlgorithm([-10,-7,-1]))