# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        m = {}
        for i in range(len(inorder)):
            m[inorder[i]] = i
        pidx = 0
        
        def build(left, right):
            nonlocal preorder
            nonlocal inorder
            nonlocal m
            nonlocal pidx
            if pidx >= len(inorder) or left>right:
                return None
            node = TreeNode(preorder[pidx])
            sepidx = m[preorder[pidx]]
            pidx += 1
            if left == right:
                return node
            leftnode = build(left, sepidx - 1)
            rightnode = build(sepidx + 1, right)
            node.left = leftnode
            node.right = rightnode
            return node
            
        return build(0, len(inorder)-1)
