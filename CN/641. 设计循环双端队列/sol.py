# https://leetcode.cn/problems/design-circular-deque/
class Node:
    def __init__(self, val=-1):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularDeque:
    def __init__(self, k: int):
        self.head = Node()
        self.end = Node()
        self.head.next = self.end
        self.end.prev = self.head
        self.capacity = k
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.size == self.capacity:
            return False
        self.size += 1
        node = Node(value)
        tmp = self.head.next
        node.next = tmp
        node.prev = self.head
        tmp.prev = node
        self.head.next = node
        return True

    def insertLast(self, value: int) -> bool:
        if self.size == self.capacity:
            return False
        self.size += 1
        node = Node(value)
        tmp = self.end.prev
        tmp.next = node
        node.prev = tmp
        node.next = self.end
        self.end.prev = node
        return True

    def deleteFront(self) -> bool:
        if self.size == 0:
            return False
        self.size -= 1
        tmp = self.head.next.next
        self.head.next = tmp
        tmp.prev = self.head
        return True


    def deleteLast(self) -> bool:
        if self.size == 0:
            return False
        self.size -= 1
        tmp = self.end.prev.prev
        tmp.next = self.end
        self.end.prev = tmp
        return True

    def getFront(self) -> int:
        if self.size == 0:
            return -1
        return self.head.next.val

    def getRear(self) -> int:
        if self.size == 0:
            return -1
        return self.end.prev.val

    def isEmpty(self) -> bool:
        return True if self.size==0 else False

    def isFull(self) -> bool:
        return True if self.size == self.capacity else False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
