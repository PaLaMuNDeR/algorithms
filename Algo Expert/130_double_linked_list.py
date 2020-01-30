# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        # Write your code here.
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def setTail(self, node):
        # Write your code here.
        if self.tail is None:
            self.tail = node
            self.head = node
            return
        self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert


def insertAfter(self, node, nodeToInsert):
    # Write your code here.
    if nodeToInsert == self.head and nodeToInsert == self.tail:
        return
    self.remove(nodeToInsert)
    nodeToInsert.prev = node
    nodeToInsert.next = node.next
    if node.next is None:
        self.tail = nodeToInsert
    else:
        node.next.prev = nodeToInsert
    node.next = nodeToInsert


def insertAtPosition(self, position, nodeToInsert):
    # Write your code here.
    if position == 1:
        self.setHead(nodeToInsert)
        return
    else:
        i = 1
        current_node = self.head
        while current_node is not None and i < position:
            i += 1
            current_node = current_node.next
        if current_node is not None:
            self.insertBefore(current_node, nodeToInsert)
        if current_node is None:
            self.setTail(nodeToInsert)


def removeNodesWithValue(self, value):
    # Write your code here.
    current_node = self.head
    while not current_node is None:
        nodeToRemove = current_node
        current_node = current_node.next
        if nodeToRemove.value == value:
            self.remove(nodeToRemove)


def remove(self, node):
    # Write your code here.
    if node == self.head:
        self.head = self.head.next
    if node == self.tail:
        self.tail = self.tail.prev
    if node.prev is not None:
        node.prev.next = node.next
    if node.next is not None:
        node.next.prev = node.prev
    node.prev = None
    node.next = None


def containsNodeWithValue(self, value):
    # Write your code here.
    current_node = self.head
    while current_node is not None:
        if current_node.value == value:
            return True
        else:
            current_node = current_node.next
    return False


def printList(self):
    current_node = self.head
    while current_node.next is not None:
        print(current_node.value)
        current_node = current_node.next