# https://leetcode.cn/problems/find-duplicate-subtrees/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# serialization of tree + hash map + set 
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        seen = {}
        repnode = set()

        def dfs(node):
            nonlocal seen
            nonlocal repnode

            if node is None:
                return ""
            seralize = "".join([str(node.val), "(", dfs(node.left), ")(", dfs(node.right), ")"])
            treenode = seen.get(seralize, None)
            if treenode:
                repnode.add(treenode)
            else:
                seen[seralize] = node
            return seralize
        dfs(root)
        # print(seen)
        return list(repnode)
