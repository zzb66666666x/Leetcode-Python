# https://leetcode.com/problems/linked-list-cycle-ii/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        slow = head
        fast = head
        while True:
            nextslow = slow.next
            if nextslow is None:
                return None
            tmp = fast.next
            if tmp is None:
                return None
            nextfast = tmp.next
            if nextfast is None:
                return None
            slow = nextslow
            fast = nextfast
            if slow == fast:
                break
        ret = head
        while ret != slow:
            ret = ret.next
            slow = slow.next
        return ret
        
