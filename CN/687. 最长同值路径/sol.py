# https://leetcode.cn/problems/longest-univalue-path/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        maxrecordever = 0
        def recur(node)-> int:
            nonlocal maxrecordever
            if node is None:
                return 0
            nodeval = node.val
            leftlen = recur(node.left)
            rightlen = recur(node.right)
            leftpath, rightpath = 0, 0
            if node.left is not None and node.left.val == nodeval:
                leftpath = leftlen + 1
            if node.right is not None and node.right.val == nodeval:
                rightpath = rightlen + 1
            maxrecordever = max(leftpath+rightpath, maxrecordever)
            return max(leftpath, rightpath)
        recur(root)
        return maxrecordever
