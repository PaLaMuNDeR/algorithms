"""
1. Implement the `Node` class to create a binary search tree. The constructor should initialize valuse `data`, `left`,
 and `right`

2. Implement the `insert` method for the Node class. Insert should accept an argument `data`, then create and insert a
 new node at the appropriate location in the tree.

3. Implement the `contains` method for the Node class. Contains should accept a `data` argument and return the Node in the tree with the same value.
If the value isn't in the tree return null.

"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
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




node1 = Node(5)
node1.insert(3)
node1.insert(6)
node1.insert(7)
print(node1.data, node1.left.data, node1.right.data, node1.right.right.data)
a = node1.contains(5)
print(a.data)