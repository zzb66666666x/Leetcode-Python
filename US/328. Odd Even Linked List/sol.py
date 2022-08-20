# https://leetcode.com/problems/odd-even-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        dummyOdd = ListNode(-1)
        dummyEven = ListNode(-1)
        ptrOdd = head
        ptrEven = head.next
        oddEnd = dummyOdd
        evenEnd = dummyEven
        while ptrOdd is not None:
            # print(ptrOdd.val)
            nextOdd = None
            nextEven = None
            if ptrEven is not None:
                # print(ptrEven.val)
                nextOdd = ptrEven.next
            if nextOdd is not None:
                nextEven = nextOdd.next
            oddEnd.next = ptrOdd
            evenEnd.next = ptrEven
            oddEnd = ptrOdd
            evenEnd = ptrEven
            ptrOdd = nextOdd
            ptrEven = nextEven
        oddEnd.next = dummyEven.next
        return dummyOdd.next
        
            
