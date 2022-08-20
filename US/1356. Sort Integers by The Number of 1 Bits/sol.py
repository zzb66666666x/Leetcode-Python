# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key=lambda x: (countOnes(x), x))
        return arr

def countOnes(val):
    mask = 1
    cnt = 0
    for _ in range(14):
        if mask & val != 0:
            cnt += 1
        mask <<= 1
    return cnt 
