# import the ListNode class
from DataStructure.list.listNode import ListNode


class LinkedListBasic:
    def __init__(self):
        self.__head = ListNode('dummy', None)
        self.__numItem = 0

    def insert():
        pass

    def append():
        pass

    def pop():
        pass

    def remove():
        pass

    def index():
        pass

    def clear():
        pass

    def count():
        pass

    def reverse():
        pass

    def sort():
        pass

    def copy():
        pass

    def extend():
        pass

    def __getNode(self, pos):
        """Returns the node at a given position."""

        if pos < 0 or pos >= self.__numItem:
            raise IndexError('list index out of range')

        else:
            currNode = self.__head.next
            for i in range(pos):
                currNode = currNode.next
            return currNode
