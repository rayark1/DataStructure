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

    def insert(self, i:int, newItem) -> None:
        """Inserts the element newItem at position i."""
        if (i >= 0 and i <= self.__numItem):
            p = self.__tail
            for j in range(i + 1):
                p = p.next
            newNode = ListNode(newItem, p.next)
            p.next = newNode
            self.__numItem += 1
        else:
            raise IndexError("List index out of range")

    def append(self, newItem) -> None:
        """Inserts the element newItem at the end of the list."""
        self.insert(self.__numItem, newItem)

    def pop(self, *args:int):
        if self.isEmpty():
            raise IndexError("List is empty")
        if len(args) != 0: # 값이 있으면 그 값이 i가 된다.
            i = args[0]
        if len(args) == 0 or i == -1: # 값이 없거나 -1이면 마지막 값이 i가 된다.
            i = self.__numItem - 1

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
