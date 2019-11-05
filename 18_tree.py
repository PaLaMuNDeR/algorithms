"""
1. Create a `Node` class. The constructor should accept an argument that gets assigned to the data property and initialize
an empty array for storing children. The node class should have methods `add` and `remove`.
2. Create a `Tree` class. The tree constructor should initialize a `root` property to null.
3. Implement `traverseBF` and `traverseDF` that would get as an input a function and apply it to all the nodes in the tree

E.g.
```
                [20]
    [0]             [40]        [-15]
[-12] [-3] [1]                   [-2]
```
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.children = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)


class Tree:

    def __init__(self):
        self.root = None


node1 = Node(20)
node11 = Node(0)
node12 = Node(40)
node13 = Node(-15)
node1.add(node11)
node1.add(node12)
node1.add(node13)

node111 = Node(12)
node112 = Node(-3)
node113 = Node(1)
node11.add(node111)
node11.add(node112)
node11.add(node113)

node131 = Node(-2)
node13.add(node131)

tree1 = Tree()
tree1.root = node1


def traverseBF(fun, node):
    """
        Traversing Breadth-First
        0. Add the root in a queue.
        While there is a queue:
            1. Add a node's children to the end of a queue.
            2. Execute the function on the first element of the queue
            3. Remove the first element of the queue. Repeat 1
    :param fun: function to be applied to all the nodes in the tree
    :param tree: the tree
    :return:
    """
    queue = []
    queue.append(node)
    while queue:
        for child in queue[0].children:
            queue.append(child)
        queue[0].data = fun(queue[0])
        queue = queue[1:]


def add10(node):
    print("Updating {0} + 10".format(node.data))
    return node.data+10


def sub10(node):
    return node.data-10


print("Value of the root before BF: {}".format(tree1.root.data))
traverseBF(add10, tree1.root)
print("Value of the root after BF: {}".format(tree1.root.data))
traverseBF(sub10, tree1.root)


def traverseDF(fun, node):
    """
        Traversing Depth-First
        0. Add the root in a list
        While there is a list:
            1. Execute the function on the node
            2. Remove the node from the list
            3. Add the node's children to the front of the list. Repeat 1


    :param fun: function to be applied to all the nodes in the tree
    :param node: the tree
    :return:
    """
    lst = [node]
    while lst:
        lst[0].data = fun(lst[0])
        lst = lst[0].children + lst[1:]

traverseDF(add10, tree1.root)
print("Value of the root after DF: {}".format(tree1.root.data))
