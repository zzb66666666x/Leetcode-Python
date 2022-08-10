# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        candidate = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(candidate)
        for i in range(k-1):
            val, r, c = heapq.heappop(candidate)
            if c != n-1:
                heapq.heappush(candidate, (matrix[r][c+1], r, c+1))
        return candidate[0][0]