from linkedListBasic import *

linkedList = LinkedListBasic()
linkedList.append(20); linkedList.insert(0, 10);
print("linkedList: ", linkedList)
a = LinkedListBasic()
a.append(1); a.append(3); a.append(2); a.append(4);
print("a: ", a)
linkedList.append(a)
print("linkedList.append(linkedList): ", linkedList)
linkedList.reverse()
print("linkedList.reverse(): ", linkedList)
linkedList.pop(0)
print("linkedList.pop(0): ", linkedList)
print("count(3): ", linkedList.count(3))
print("get(3): ", linkedList.get(3))