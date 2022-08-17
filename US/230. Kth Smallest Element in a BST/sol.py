# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        rank = 0
        ans = -1
        def dfs(node):
            nonlocal rank
            nonlocal ans
            nonlocal k
            if node is None:
                return -1
            if dfs(node.left) == 0:
                return 0
            rank += 1
            if rank == k:
                ans = node.val
                return 0
            if dfs(node.right) == 0:
                return 0
            return -1
        dfs(root)
        return ans
