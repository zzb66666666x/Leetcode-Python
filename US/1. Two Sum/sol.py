# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(nums)):
            m[nums[i]] = i
        for i in range(len(nums)):
            val = nums[i]
            nextone = target - val
            if nextone in m and m[nextone] != i:
                return [i, m[nextone]]
        return None # not triggered
