# import the ListNode class
from listNode import ListNode


class CircularLinkedList:
    """This class implements a linked list data structure."""

    def __init__(self):
        self.__tail = ListNode('dummy', None)
        self.__tail.next = self.__tail
        self.__numItem = 0

    def __iter__(self):
        """Returns the list's iterator for traversing the list."""

        return CircularLinkedListIterator(self.__tail)


class CircularLinkedListIterator:
    """This class implements an iterator for a circular linked list."""

    def __init__(self, tail):
        self.__tail = tail
        self.__currNode = tail.next

    def __iter__(self):
        return self

    def __next__(self):
        if self.__currNode == self.__tail:
            raise StopIteration
        else:
            item = self.__currNode.item
            self.__currNode = self.__currNode.next
            return item
