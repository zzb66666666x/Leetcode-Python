# https://leetcode.com/problems/longest-consecutive-sequence/
# classic union find approach
class UF:
    def __init__(self, nums):
        self.parent = {}
        self.size = {}
        self.count = len(nums)
        for val in nums:
            self.parent[val] = val
            self.size[val] = 1
        
    def find(self, x):
        if x not in self.parent:
            return None
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)
        if rootp is None or rootq is None:
            return
        if rootp == rootq:
            return
        if self.size[rootp] < self.size[rootq]:
            self.parent[rootp] = rootq
            self.size[rootq] += self.size[rootp]
        else:
            self.parent[rootq] = rootp
            self.size[rootp] += self.size[rootq]
        self.count -= 1
        

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uf = UF(nums)
        # print(uf.parent)
        for val in nums:
            uf.union(val, val+1)
            uf.union(val, val-1)
            # print(val)
            # print(uf.parent)
            # print("#############")
        ret = 0
        for k,v in uf.size.items():
            if v>ret:
                ret = v
        return ret
