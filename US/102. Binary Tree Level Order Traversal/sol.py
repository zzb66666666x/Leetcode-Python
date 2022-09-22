# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        if root is None:
            return ret
        q = deque()
        q.append([root])
        while len(q)>0:
            nextone = []
            curlevel = q.popleft()
            val = []
            for node in curlevel:
                val.append(node.val)
                if node.left is not None:
                    nextone.append(node.left)
                if node.right is not None:
                    nextone.append(node.right)
            ret.append(val)
            if len(nextone)>0:
                q.append(nextone)
        return ret
        
                    
