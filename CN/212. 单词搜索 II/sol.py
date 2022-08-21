# https://leetcode.cn/problems/word-search-ii/
class Trie:
    class TrieNode:
        def __init__(self):
            self.tns = [None for i in range(26)]
            self.word = None
            
    def __init__(self, words = []):
        self.root = self.TrieNode()
        for word in words:
            self.add(word)
        
    def add(self, s):
        node = self.root
        for c in s:
            idx = ord(c) - ord('a')
            if node.tns[idx] is None:
                node.tns[idx] = self.TrieNode()
            node = node.tns[idx]
        node.word = s
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie(words)
        trienode = trie.root
        m = len(board)
        n = len(board[0])
        res = set()
        def dfs(board, r, c, tnode, res):
            m = len(board)
            n = len(board[0])
            if r<0 or c<0 or r>=m or c>=n:
                return
            ch = board[r][c]
            if ch=='#':
                return
            nextnode = tnode.tns[ord(ch)-ord('a')]
            if nextnode is not None:
                board[r][c] = '#'
                if nextnode.word is not None:
                    res.add(nextnode.word)
                dfs(board, r+1, c, nextnode, res)
                dfs(board, r-1, c, nextnode, res)
                dfs(board, r, c-1, nextnode, res)
                dfs(board, r, c+1, nextnode, res)
                board[r][c] = ch
            else:
                return
        for i in range(m):
            for j in range(n):
                dfs(board, i, j, trienode, res)
        return list(res)
