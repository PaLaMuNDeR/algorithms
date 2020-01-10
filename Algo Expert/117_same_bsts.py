"""
Same BSTs
An array of integers is said to represent the Binary Search Tree (BST) obtained by inserting each integer in the array (from left to right) into the BST. Write a function that takes in two arrays of integers and returns a boolean representing whether or not these arrays represent the same BST. Note that you are not allowed to construct any BSTs in your code. A BST is a Binary Tree that consists only of BST nodes. A node is said to be a BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; and both of its children nodes are either BST nodes themselves or None (null) values.
Sample input: [10, 15, 8, 12, 94, 81, 5, 2, 11], [10, 8, 5, 15, 2, 12, 11, 94, 81] Sample output: True

"""

def sameBsts(arrayOne, arrayTwo):
    # Write your code here.
    if len(arrayOne) != len(arrayTwo):
        return False

    if len(arrayOne) == 0:
        return True

    if arrayOne[0] != arrayTwo[0]:
        return False

    leftOne = getSmaller(arrayOne)
    rightOne = getBigger(arrayOne)
    leftTwo = getSmaller(arrayTwo)
    rightTwo = getBigger(arrayTwo)
    return sameBsts(leftOne, leftTwo) and sameBsts(rightOne, rightTwo)


def getSmaller(array):
    root = array[0]
    result = []
    for i in array:
        if i < root:
            result.append(i)

    return result


def getBigger(array):
    if len(array) == 0:
        return None
    root = array[0]
    result = []
    for i in array[1:]:
        if i >= root:
            result.append(i)
    return result

