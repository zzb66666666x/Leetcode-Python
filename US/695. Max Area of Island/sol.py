# https://leetcode.com/problems/max-area-of-island/

# method1: dfs
# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         m = len(grid)
#         n = len(grid[0])
#         vis = [[False for j in range(n)] for i in range(m)]
        
#         def dfs(i, j):
#             nonlocal vis
#             nonlocal grid
#             nonlocal m
#             nonlocal n
#             if i<0 or j<0 or i>=m or j>=n:
#                 return 0
#             if grid[i][j] == 0 or vis[i][j]:
#                 return 0
#             vis[i][j] = True
#             a = dfs(i+1, j)
#             b = dfs(i, j+1)
#             c = dfs(i-1, j)
#             d = dfs(i, j-1)
#             return 1+a+b+c+d
        
#         ret = 0
#         for i in range(m):
#             for j in range(n):
#                 ret = max(ret, dfs(i,j))
#         return ret
    
#method2: union find
class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]
        self.count = n
        
    def union(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)
        if rootp == rootq:
            return
        if self.size[rootp]<self.size[rootq]:
            self.parent[rootp] = rootq
            self.size[rootq] += self.size[rootp]
        else:
            self.parent[rootq] = rootp
            self.size[rootp] += self.size[rootq]
        self.count -= 1
    
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        uf = UF(m*n)
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        flag = False
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    flag = True
                    idx = i*n + j
                    for d in dirs:
                        ni, nj = i+d[0], j+d[1]
                        if ni<0 or nj<0 or ni>=m or nj>=n:
                            continue
                        if grid[ni][nj] == 1:
                            nidx = ni*n + nj
                            uf.union(idx, nidx)
        if not flag:
            return 0
        ret = 0
        for val in uf.size:
            ret = max(ret, val)
        return ret
        
        
