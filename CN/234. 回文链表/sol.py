# https://leetcode.cn/problems/palindrome-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        length = 0
        tmp = head
        while tmp is not None:
            tmp = tmp.next
            length += 1
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        # reverse linked list
        if length % 2 == 1:
            slow = slow.next
        slow = self.reverse(slow)
        for _ in range(length//2):
            if head.val != slow.val:
                return False
            slow = slow.next
            head = head.next
        return True

    def reverse(self, head):
        dummy = ListNode(-1)
        nextnode = None
        while head is not None:
            tmp = head.next
            dummy.next = head
            head.next = nextnode
            nextnode = head
            head = tmp
        return dummy.next

        
        
