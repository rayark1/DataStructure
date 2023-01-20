# import the ListNode class
from listNode import ListNode


class CircularLinkedList:
    """This class implements a linked list data structure."""

    def __init__(self):
        self.__tail = ListNode('dummy', None)
        self.__tail.next = self.__tail
        self.__numItem = 0