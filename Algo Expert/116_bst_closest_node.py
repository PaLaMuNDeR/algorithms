"""
Find Closest Value In BST
You are given a BST data structure consisting of BST nodes. Each BST node has an integer value stored in a property
called "value" and two children nodes stored in properties called "left" and "right," respectively.
A node is said to be a BST node if and only if it satisfies the BST property: its value is strictly greater than the
values of every node to its left; its value is less than or equal to the values of every node to its right;
and both of its children nodes are either BST nodes themselves or None (null) values.

You are also given a target integer value; write a function that finds the closest value to that target value contained
in the BST. Assume that there will only be one closest value.
Sample input: 10 ,12 / \ 5 15 / \ / \ 2 513 22 / \ 1 14 Sample output: 13

"""
def findClosestValueInBst(tree,target):
    return findClosestValueInBstHelper(tree, target, float("inf"))

def findClosestValueInBstHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target-tree.value):
        closest = tree.value

    if target < tree.value:
        return findClosestValueInBstHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBstHelper(tree.right, target, closest)
    else:
        return closest

