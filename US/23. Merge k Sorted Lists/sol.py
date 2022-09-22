# https://leetcode.com/problems/merge-k-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Status:
    def __init__(self, val, node):
        self.val = val
        self.node = node

    def __lt__(self, other):
        return self.val<other.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        h = []
        for node in lists:
            if node is not None:
                heapq.heappush(h, Status(node.val, node))
        head = ListNode(0)
        tail = head
        while len(h)>0:
            status = heapq.heappop(h)
            nodeptr = status.node
            tail.next = nodeptr
            tail = nodeptr
            if nodeptr.next is not None:
                heapq.heappush(h, Status(nodeptr.next.val, nodeptr.next))
        return head.next
