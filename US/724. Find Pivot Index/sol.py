# https://leetcode.com/problems/find-pivot-index/
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        tmp = 0
        for i in range(len(nums)):
            tmp += nums[i]
            if tmp == total-tmp+nums[i]:
                return i
        return -1
