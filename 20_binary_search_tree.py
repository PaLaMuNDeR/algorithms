"""
1. Implement the `Node` class to create a binary search tree. The constructor should initialize valuse `data`, `left`,
 and `right`

2. Implement the `insert` method for the Node class. Insert should accept an argument `data`, then create and insert a
 new node at the appropriate location in the tree.

3. Implement the `contains` method for the Node class. Contains should accept a `data` argument and return the Node in the tree with the same value.
If the value isn't in the tree return null.

4. Validate the Binary Search Tree - given a node, validate the binary search tree, ensuring that every node's left hand
 child is less than the parent node's value, and that every node's right hand child is greater than the parent

"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        """ Insert new node to left or right """
        newNode = Node(data)

        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = newNode
        elif data > self.data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = newNode
        elif data == self.data:
            "This node already exists"

    def contains(self, data):
        """ Check if data is already contained in the tree"""
        if data == self.data:
            return self
        if data < self.data:
            if self.left:
                return self.left.contains(data)
            else:
                return None
        if data > self.data:
            if self.right:
                return self.right.contains(data)
            else:
                return None

    def validate(self, min=None, max=None):
        """
            Option 1 - Using the version from the course:
            Use min and max to validate if each node is within the proper limits
        """
        print("checking for: {}. with min: {} and max: {} ".format(self.data, min, max))
        if min and self.data <= min:
            return False
        if max and self.data >= max:
            return False
        if self.left:
            if self.left.data < self.data:
                update_max = self.data
                return self.left.validate(min, max=update_max)
            else:
                return False
        if self.right:
            if self.right.data > self.data:
                update_min = self.data
                return self.right.validate(min=update_min, max=max)
            else:
                return False
        return True

    def validate_option_2(self):
        """
            Validate Option 2:
            Recursion where we check for all the values under.
        """
        print("Option 2: checking for: {}. ".format(self.data))

        right = False
        if self.left:
            if self.left < self.data:
                left = True
                return left and self.left.validate_option_2()
            else:
                return False
        else:
            left = True

        if self.right:
            if self.right > self.data:
                right = True
                return right and self.right.validate_option_2()
        else:
            right = True

        return left and right


node1 = Node(5)
node1.insert(3)
node1.insert(6)
node1.insert(7)
print(node1.data, node1.left.data, node1.right.data, node1.right.right.data)
a = node1.contains(5)
print(a.data)

print("Validate a valid Tree Option 1:")
print(node1.validate())

import time
time.sleep(3)
print("Validate a valid Tree Option 2:")
print(node1.validate_option_2())
time.sleep(3)

node_b_1 = Node(5)
node_b_2 = Node(3)
node_b_3 = Node(6)
node_b_4 = Node(7)

node_b_1.left = node_b_2
node_b_1.right = node_b_3
# Putting node 4 on a wrong spot on purpose to check the validation
node_b_2.right = node_b_4

print("Validate a broken Tree Option 1:")
print(node_b_1.validate())
time.sleep(3)

print("Validate a broken Tree Option 2:")
print(node_b_1.validate_option_2())
