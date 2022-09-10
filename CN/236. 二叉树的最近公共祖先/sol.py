# https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ret = None
        def dfs(node, pval, qval):
            nonlocal ret
            if node is None:
                return 0
            left = dfs(node.left, pval, qval)
            right = dfs(node.right, pval, qval)
            if ret is not None:
                return 2
            if node.val == pval or node.val == qval:
                if left+right == 1:
                    ret = node
                    return 2
                else:
                    if left+right != 0:
                        print("something wrong")
                    return 1
            else:
                if left+right == 2:
                    ret = node
                    return 2
                elif left+right == 1:
                    return 1
                else:
                    return 0
        dfs(root, p.val, q.val)
        return ret
