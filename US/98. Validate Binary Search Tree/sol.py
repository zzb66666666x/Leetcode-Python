# https://leetcode.com/problems/validate-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# method1: updating bounds
# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         def helper(node, lower = float('-inf'), upper = float('inf')) -> bool:
#             if not node:
#                 return True
            
#             val = node.val
#             if val <= lower or val >= upper:
#                 return False

#             if not helper(node.right, val, upper):
#                 return False
#             if not helper(node.left, lower, val):
#                 return False
#             return True
#         return helper(root)

#method2: in order traverse
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        pre = float("-inf")
        def recur(node):
            nonlocal pre
            if node is None:
                return True
            if not recur(node.left):
                return False
            if node.val <= pre:
                return False
            pre = node.val
            return recur(node.right)
        return recur(root)
