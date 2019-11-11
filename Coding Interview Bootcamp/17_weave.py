"""
1. Implement - `peek` , `add` and `remove` functions to a Queue. `remove` should remove the first element of the queue. `peek` should print out the first item of the queue without removing it.
2. Implement a `weave` function that merges two stacks into a third one with alternating content. The function should handle queues of different lengths. Only use `add`, `remove` and `queue`. Do not use the array

Example:
    QueueOne.add(1)
    QueueOne.add(2)
    QueueOne.add(3)
    QueueOne.add('hi')
    QueueOne.add('there)

    weaveList = weave(QueueOne, QueueTwo)
    weaveList.remove() // 1
    weaveList.remove() // 'hi'
    weaveList.remove() // 2
    weaveList.remove() // 'there'
    weaveList.remove() // 3

"""


class Node:

    def __init__(self, data=None):
        self.data = data
        self.nextval = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertLast(self, newdata):
        """
            Inserts an element at the end.
        :param newdata: data of the new element
        """
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return
        last = self.head

        while last.nextval:
            last = last.nextval

        last.nextval = NewNode

    def listprint(self):
        """
            Prints the list
        """
        printval = self.head
        while printval:
            print(printval.data)
            printval = printval.nextval

    def peekLast(self):
        """
            Prints the last element
        """
        last_node = self.head
        if not last_node:
            print(' ')
        else:
            if last_node.nextval:
                next_element = last_node.nextval

                while next_element:
                    last_node = last_node.nextval
                    next_element = last_node.nextval

            print(last_node.data)

    def pop(self):
        """
            Removes the last elements and prints it
        """
        last_node = self.head
        if not last_node:
            print(' ')
            return None
        else:
            if last_node.nextval:
                next_element = last_node.nextval
                previous_element = last_node

                while next_element:
                    previous_element = last_node
                    last_node = last_node.nextval
                    next_element = last_node.nextval

                previous_element.nextval = None
                print(last_node.data)
                return last_node.data

    # === Solutions for the task
    def add(self, newdata):
        """
            Add new head element
        """
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return
        else:
            last_head = self.head
            NewNode.nextval = last_head
            self.head = NewNode

    def peek(self):
            """
                Add new head element
            """
            if self.head is None:
                print("")
            else:
                print(self.head.data)

    def remove(self):
        """
            Remove the head
        """
        if self.head is None:
            print("")
        else:
            if self.head.nextval:
                self.head.data = self.head.nextval.data
                self.head.nextval = self.head.nextval.nextval
            else:
                self.head.data = None


def weave(list1, list2):
    """ Merges two lists into a third list."""
    list3 = LinkedList()
    while list1.head.data and list2.head.data:
        list3.insertLast(list1.head.data)
        list3.insertLast(list2.head.data)
        list1.remove()
        list2.remove()

    while list1.head.data:
        list3.insertLast(list1.head.data)
        list1.remove()
    while list2.head.data:
        list3.insertLast(list2.head.data)
        list2.remove()

    return list3



QueueOne = LinkedList()
QueueOne.insertLast(1)
QueueOne.insertLast(2)
QueueOne.insertLast(3)
QueueOne.insertLast(4)
QueueOne.add('a')
# QueueOne.pop()
# QueueOne.listprint()
# QueueOne.peekLast()
# QueueOne.peek()
QueueOne.remove()
# QueueOne.listprint()


QueueTwo = LinkedList()
QueueTwo.insertLast('hi')
QueueTwo.insertLast('there')

weaveList = weave(QueueOne, QueueTwo)
weaveList.listprint()
