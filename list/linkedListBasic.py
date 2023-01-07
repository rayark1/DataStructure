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

    def pop(self, pos):
        """Removes and returns the item at the given position."""

        if pos < 0 or pos >= self.__numItem:
            raise IndexError('list index out of range')

        else:
            targetNode = __getNode(self, pos-1)
            item = targetNode.next.item
            targetNode.next = targetNode.next.next
            self.__numItem -= 1
            return item

    def remove(self, item):
        """Removes the first occurrence of item."""

        currNode = self.__head
        while currNode.next != None:
            if currNode.next.item == item:
                currNode.next = currNode.next.next
                self.__numItem -= 1
                return
            currNode = currNode.next

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

    def reverse():
        pass

    def sort():
        pass

        pass


    def copy(self) -> LinkedListBasic():
        """Returns a copy of the list."""

        copy = LinkedListBasic()
        for i in range(self.__numItem):
            copy.append(self.get(i))
        return copy

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
