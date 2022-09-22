
# https://leetcode.cn/problems/number-of-operations-to-make-network-connected/
class UF:
    def __init__(self, n):
        self.count = n
        self.size = [1 for i in range(n)]
        self.parent = [i for i in range(n)]
    
    def union(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)
        if rootp == rootq:
            return
        if self.size[rootp] < self.size[rootq]:
            self.parent[rootp] = rootq
            self.size[rootq] += self.size[rootp]
        else:
            self.parent[rootq] = rootp
            self.size[rootp] += self.size[rootq]
        self.count -= 1
            

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def connected(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)
        if rootp == rootq:
            return True
        else:
            return False

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        uf = UF(n)
        quota = 0
        ops = 0
        for conn in connections:
            p, q = conn[0], conn[1]
            if uf.connected(p, q):
                quota += 1
            else:
                uf.union(p, q)
        # print(quota)
        # print(uf.count)
        ops = uf.count - 1
        return -1 if ops>quota else ops
