# https://leetcode.cn/problems/lru-cache/
class DNode:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.data = {}
        self.capacity = capacity
        self.head = DNode()
        self.end = DNode()
        self.head.next = self.end
        self.end.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        else:
            node = self.data[key]
            ret = node.val
            self.removeNode(node)
            self.addFirst(node)
            return ret


    def put(self, key: int, value: int) -> None:
        # print(key, value)
        if key in self.data:
            node = self.data[key]
            node.val = value
            self.removeNode(node)
            self.addFirst(node)
        else:
            newnode = DNode(key, value)
            if len(self.data) + 1 > self.capacity:
                oldkey = self.end.prev.key
                # print(oldkey)
                self.data.pop(oldkey)
                self.removeLast()
                # print(self.end.prev.key)
                self.addFirst(newnode)
                self.data[key] = newnode
            else:
                self.addFirst(newnode)
                self.data[key] = newnode

    def removeNode(self, node):
        nextone = node.next
        prevone = node.prev
        prevone.next = nextone
        nextone.prev = prevone

    def addFirst(self, node):
        tmp = self.head.next
        self.head.next = node
        node.prev = self.head
        tmp.prev = node
        node.next = tmp

    def removeLast(self):
        if self.head.next == self.end:
            return
        tmp = self.end.prev.prev
        tmp.next = self.end
        self.end.prev = tmp

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
