"""
Reverse Linked List
Write a function that takes in the head of a Singly Linked List (assume that the list has at least 1 node; in other words, the head will never be a null value). The function should reverse the list and return its new head. Note that every node in the Singly Linked List has a "value" property storing its value as well as a "next" property pointing to the next node in the list or None (null) if it is the tail of the list.
Sample input: 0 -> 1 -> 2 -> 3 -> 4 -> 5 (the head node with value 0) Sample output: 5 -> 4 -> 3 -> 2 -> 1 -> 0 (the new head node with value 5)

"""

def reverseLinkedList(head):
    p1, p2 = None, head
    while p2 is not None:
        p3 = p2.next
        p2.next = p1
        p1 = p2
        p2 = p3
    return p1