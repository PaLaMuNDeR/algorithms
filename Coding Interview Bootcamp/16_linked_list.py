"""
Return the middle node of a Linked list.
If the list has an even number of elements, return the node
at the end of the first half of the list.
DO NOT use a counter variable, DO NOT retrieve the size of the list,
and only iterate through the list one time.

Example:
    const l = LinkedL()
    l.insertLast('a')
    l.insertLast('b')
    l.insertLast('c')
    midpoint(l) -> { data: 'b' }

"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.nextval = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertLast(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return
        last = self.head

        while last.nextval:
            last = last.nextval

        last.nextval = NewNode

    def listprint(self):
        printval = self.head
        while printval:
            print(printval.data)
            printval = printval.nextval


def midpoint(linkedL):
    """
        We create two iterators.
        One is jumping one step at a time
        The other is jumping two steps at a time.
        If in front of the second iterator the next 2 values are None,
        then the first iterator has reached the midpoint
    """

    head = linkedL.head

    i = linkedL.head
    j = linkedL.head

    while j:
        if j.nextval and j.nextval.nextval:
            i = i.nextval
            j = j.nextval.nextval
        else:
            return i.data


linkedL = LinkedList()
node1 = Node('a')
linkedL.head = node1
# print(linkedL.head.nextval.data)
linkedL.listprint()
print "Answer"
print midpoint(linkedL)