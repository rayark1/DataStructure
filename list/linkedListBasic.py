# import the ListNode class
from listNode import ListNode


class LinkedListBasic:
    """This class implements a linked list data structure."""

    def __init__(self):
        self.__head = ListNode('dummy', None)
        self.__numItem = 0

    def insert(self, pos: int, item):
        """Inserts an item at a given position."""

        if pos >= 0 and pos <= self.__numItem:
            targetNode = self.__getNode(pos-1)
            newNode = ListNode(item, targetNode.next)
            targetNode.next = newNode
            self.__numItem += 1

        else:
            raise IndexError('list index out of range')

    def append(self, item):
        """Appends an item to the end of the list."""

        self.insert(self.__numItem, item)

    def pop(self, pos):
        """Removes and returns the item at the given position."""

        if self.isEmpty():
            raise IndexError('list is empty')

        if pos >= 0 and pos <= self.__numItem:
            targetNode = self.__getNode(pos-1)
            item = targetNode.next.item
            targetNode.next = targetNode.next.next
            self.__numItem -= 1
            return item

        else:
            raise IndexError('list index out of range')

    def remove(self, item):
        """Removes the first occurrence of item."""

        currNode = self.__head
        while currNode.next != None:
            if currNode.next.item == item:
                currNode.next = currNode.next.next
                self.__numItem -= 1
                return
            currNode = currNode.next

    def get(self, pos):
        """Returns the item at the given position."""

        if pos < 0 or pos >= self.__numItem:
            raise IndexError('list index out of range')
        elif self.isEmpty():
            raise IndexError('list is empty')
        else:
            return self.__getNode(pos).item

    def index(self, item):
        """Returns the position of the first occurrence of item."""

        currNode = self.__head.next
        for i in range(self.__numItem):
            if currNode.item == item:
                return i
            currNode = currNode.next
        raise ValueError('list.index(x): x not in list')

    def clear(self):
        """Removes all items from the list."""

        self.__head.next = None
        self.__numItem = 0

    def isEmpty(self):
        """Returns True if the list is empty, False otherwise."""

        return self.__numItem == 0

    def size(self):
        """Returns the number of items in the list."""

        return self.__numItem

    def count(self, item):
        """Returns the number of occurrences of item."""

        count = 0
        currNode = self.__head.next
        for i in range(self.__numItem):
            if currNode.item == item:
                count += 1
            currNode = currNode.next
        return count

    def reverse(self):
        """Reverses the items in the list."""

        a = LinkedListBasic()
        for i in range(self.__numItem):
            a.insert(0, self.get(i))
        self.clear()
        for i in range(a.__numItem):
            self.append(a.get(i))

    def sort(self) -> None:
        """Sorts the list in ascending order."""

        a = []
        for i in range(self.__numItem):
            a.append(self.pop(0))
        a.sort()
        for i in range(len(a)):
            self.append(a[i])

    def copy(self) -> 'LinkedListBasic()':
        """Returns a copy of the list."""

        copy = LinkedListBasic()
        for i in range(self.__numItem):
            copy.append(self.get(i))
        return copy

    def extend(self, extendList):
        """Appends the items from extendList to the end of the list."""

        for i in range(extendList.size()):
            self.append(extendList.get(i))

    def __getNode(self, pos: int):
        """Returns the node at a given position."""

        currNode = self.__head
        for i in range(pos + 1):
            currNode = currNode.next
        return currNode
