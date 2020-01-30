"""
Merge Linked Lists
Write a function that takes in the heads of two Singly Linked Lists that are in sorted order, respectively (assume that the lists have at least 1 node; in other words, the heads will never be null values). The function should merge the lists and return the head of the merged list; the merged list should be in sorted order. Note that every node in the Singly Linked Lists has a "value" property storing its value as well as a "next" property pointing to the next node in the list or None (null) if it is the tail of the list.
Sample input:
2 -> 6 -> 7 -> 8 (the head node with value 2) 1 -> 3 -> 4 -> 5 -> 9 -> 10 (the head node with value 1)
Sample output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 (the new head node with value 1)

"""

def mergeLinkedLists(head1, head2):
    p1, p2, p3, p4 = head1, head2, head1.next, head2.next
    original_head = head1
    if p1.value > p2.value:
        p1,p2,p3,p4 = head2, head1, head2.next, head1.next
        original_head = head2
    while p1 is not None and p2 is not None:
        if p1 is not None and p2 is not None and p3 is not None and p1.value <= p2.value and p2.value <= p3.value:
            p1.next = p2
            p2.next = p3

            p1 = p2
            p2 = p4
            if p4 is not None:
                p4 = p4.next
        else:
            if p3 is None:
                if p2 is not None:
                    p1.next = p2
                    return original_head
            elif p3.next is not None:
                p1 = p1.next
                p3 = p3.next
            else:
                p3.next = p2
                return original_head

    return original_head