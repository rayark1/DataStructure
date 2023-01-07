# import the ListNode class
from DataStructure.list.listNode import ListNode


class LinkedListBasic:
    def __init__(self):
        self.__head = ListNode('dummy', None)
        self.__numItem = 0

    def insert(self, item, pos):
        """Inserts an item at a given position."""

        if pos < 0 or pos > self.__numItem:
            raise IndexError('list index out of range')

        else:
            targetNode = __getNode(self, pos-1)
            newNode = ListNode(item, targetNode.next)
            targetNode.next = newNode
            self.__numItem += 1

    def append(self, item):
        """Appends an item to the end of the list."""

        self.insert(item, self.__numItem)

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
