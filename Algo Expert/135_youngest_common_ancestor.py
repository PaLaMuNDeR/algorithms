"""
 Youngest Common Ancestor
You're given three inputs, all of which are instances of a class that have an "ancestor" property pointing to their youngest ancestor. The first input is the top ancestor in an ancestral tree (i.e., the only instance that has no ancestor), and the other two inputs are descendants in the ancestral tree. Write a function that returns the youngest common ancestor to the two descendants.
Sample input: Node A, Node E, Node I (from the ancestral tree below)
``` A
   /  \
  B    C
 / \  / \
 D E F   G
/\
H I
```
"""

class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = depthTwo = 0
    node = descendantOne
    while node is not topAncestor:
        depthOne += 1
        node = node.ancestor

    node = descendantTwo
    while node is not topAncestor:
        depthTwo += 1
        node = node.ancestor

    while depthOne > depthTwo and descendantOne is not topAncestor:
        descendantOne = descendantOne.ancestor

    while depthTwo > depthOne and descendantTwo is not topAncestor:
        descendantTwo = descendantTwo.ancestor

    while descendantOne is not descendantTwo:
        descendantOne = descendantOne.ancestor
        descendantTwo = descendantTwo.ancestor

    return descendantOne