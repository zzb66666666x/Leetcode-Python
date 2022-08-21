# https://leetcode.com/problems/merge-two-sorted-lists/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = list1
        ptr2 = list2
        dummy = ListNode()
        end = dummy
        while (ptr1 is not None) and (ptr2 is not None):
            if ptr1.val < ptr2.val:
                end.next = ptr1
                end = ptr1
                ptr1 = ptr1.next
            else:
                end.next = ptr2
                end = ptr2
                ptr2 = ptr2.next
        while ptr1 is not None:
            end.next = ptr1
            end = ptr1
            ptr1 = ptr1.next
        while ptr2 is not None:
            end.next = ptr2
            end = ptr2
            ptr2 = ptr2.next
        return dummy.next
