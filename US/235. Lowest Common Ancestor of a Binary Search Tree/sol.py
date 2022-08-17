# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recur(node, val, path):
            if node is None:
                return
            path.append(node)
            if node.val == val:
                return
            if node.val > val:
                recur(node.left, val, path)
            else:
                recur(node.right, val, path)
        path1, path2 = [], []
        recur(root, p.val, path1)
        recur(root, q.val, path2)
        ret = root
        for i in range(min(len(path1), len(path2))):
            if path1[i].val == path2[i].val:
                ret = path1[i]
            else:
                break
        return ret
