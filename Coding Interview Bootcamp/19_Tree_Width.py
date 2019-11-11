"""
Given the root node of a tree, return an array where each element is the width of tree at each level

Example:
```
Given:
    0
/   |   \
1   2   3
|       |
4       5

Answer: [1,3,2]
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


# node1 = Node(0)
# node11 = Node(1)
# node12 = Node(2)
# node13 = Node(3)
# node1.add(node11)
# node1.add(node12)
# node1.add(node13)
#
# node111 = Node(4)
# node11.add(node111)
#
# node131 = Node(5)
# node13.add(node131)
#
# tree1 = Tree()
# tree1.root = node1


# The definition of the bigger tree from the previous exercise
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


def level_width(node):
    """
        That's a slight variation of the proposed answer.
        Count the amount of nodes we see in a counter.
        We add the root node to the answer array.
        While the counter is greater than 0 we will run the following:
            For each element in answer:
            1. Reduce the counter
            For each child of the node:
                1.1 Insert a node's children in the `next_level` array
                1.2 Increase the counter of nodes we met
            2. Count the amount of elements at the current level and overwrite them at the same level -
            2. Insert `next_level` array to `answer`

    """
    answer = []
    answer.append([node])
    level = 0  # The current level
    counter = 1  # The amount of nodes we have seen
    while counter > 0:
        # Iterate once for every element we have seen

        next_level = []

        for elem in answer[level]:
            # for each element in the current level reduce the counter
            counter = counter - 1

            for child in elem.children:
                # if the element has children, append them to the next_level list
                next_level.append(child)
                # Hey, we saw new node, so we increase the counter
                counter += 1

        # Job is done for this level
        # Count the amount of elements on this level and store them at the proper position
        answer[level] = len(answer[level])

        # If we found some children, append them to the answer and increase the level
        if next_level:
            answer.append(next_level)
            level += 1

    return answer


print(level_width(node1))