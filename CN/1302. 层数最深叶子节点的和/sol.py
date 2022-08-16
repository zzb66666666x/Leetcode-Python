# https://leetcode.cn/problems/deepest-leaves-sum/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        nodelistdep = 0
        def recur(node, depth, nodelist):
            nonlocal nodelistdep
            if node is None:
                return nodelist
            if node.left is None and node.right is None:
                if depth > nodelistdep:
                    nodelistdep = depth
                    return [node.val]
                elif depth == nodelistdep:
                    nodelist.append(node.val)
                    return nodelist
            nodelist = recur(node.left, depth+1, nodelist)
            nodelist = recur(node.right, depth+1, nodelist)
            return nodelist
        return sum(recur(root, 0, []))
