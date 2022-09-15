# https://leetcode.com/problems/n-ary-tree-level-order-traversal/
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return None
        q = deque([root])
        ret = []
        while q:
            cnt = len(q)
            level = []
            for _ in range(cnt):
                head = q.popleft()
                level.append(head.val)
                for node in head.children:
                    q.append(node)
            ret.append(level)
        return ret
