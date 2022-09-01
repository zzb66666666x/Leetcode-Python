# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ret = 0
        def recur(node, maxval):
            nonlocal ret
            if node is None:
                return 
            if node.val >= maxval:
                maxval = node.val
                ret += 1
            recur(node.left, maxval)
            recur(node.right, maxval)
        recur(root, -100000)
        return ret
            
                
            
        
