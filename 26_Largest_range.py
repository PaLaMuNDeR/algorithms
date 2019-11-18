"""
Largest Range
Write a function that takes in an array of integers and returns an array of length 2 representing the largest range of numbers contained in that array. The first number in the output array should be the first number in the range while the second number should be the last number in the range. A range of numbers is defined as a set of numbers that come right after each other in the set of real integers. For instance, the output array [2, 6] represents the range {2, 3, 4, 5, 6}, which is a range of length 5. Note that numbers do not need to be ordered or adjacent in the array in order to form a range. Assume that there will only be one largest range.
Sample input: [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6] Sample output: [0, 7]

"""

# Time: O(n*log(n)) | Space: (n)
def largestRange(array):
    """ Solution with arrays """
    array.sort()
    arr=[]
    current_solution = []
    best_solution = []
    for i in range(0, len(array)):
        if i+1 < len(array):
            if array[i] != array[i+1]:
                arr.append(array[i])
        else:
            arr.append(array[i])

    print arr
    for i in range(0, len(arr)):
        if i+1 < len(arr):
            if arr[i] + 1 == arr[i+1]:
                current_solution.append(arr[i])
            else:
                current_solution.append(arr[i])
                if len(current_solution) > len(best_solution):
                    best_solution = current_solution
                current_solution = []
        else:
            current_solution.append(arr[i])

        if len(current_solution) > len(best_solution):
            best_solution = current_solution
    return [best_solution[0], best_solution[-1]]


# Time O(n) | Space O(n)
def largestRange(arr):
    dict = {}
    for i in arr:
        dict[i] = True # Not Visited

    current_solution = [None, None]
    best_solution = []
    best_length = 0

    def check_left(d):
        if d in dict.keys():
            if dict[d]:
                dict[d] = False
                current_solution[0] = d
                check_left(d - 1)

    def check_right(d):
        if d in dict.keys():
            if dict[d]:
                dict[d] = False
                current_solution[1] = d
                check_right(d + 1)

    for i in dict.keys():
        if dict[i]:
            current_solution = [i,i]
            dict[i] = False
            check_left(i-1)
            check_right(i+1)
            current_length = current_solution[1]-current_solution[0]
            if current_length >= best_length:
                best_solution = current_solution
                best_length = current_length

    return best_solution



arr = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6,13,14,16,17,18,19,20]
print(largestRange(arr))