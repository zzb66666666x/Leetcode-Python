# https://leetcode.com/problems/rotate-image/
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rOffset = 0
        cOffset = 0
        n = len(matrix)
        # print(n)
        while n>1:
            for i in range(n-1):
                r, c = 0, i
                # print(r,c)
                oldval = matrix[r + rOffset][c + cOffset]
                for cnt in range(4):
                    tmp = i
                    nextround = (cnt+1)%4
                    if nextround == 1:
                        tmp = n-1
                    elif nextround == 2:
                        tmp = n-1-i
                    elif nextround == 3:
                        tmp = 0
                    # print("next:", c+rOffset, tmp+cOffset)
                    val = matrix[c + rOffset][tmp + cOffset]
                    matrix[c + rOffset][tmp + cOffset] = oldval
                    oldval = val
                    r, c = c, tmp
            n -= 2
            rOffset += 1
            cOffset += 1
        
        
