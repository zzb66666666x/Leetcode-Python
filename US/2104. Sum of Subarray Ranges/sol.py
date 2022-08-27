# https://leetcode.com/problems/sum-of-subarray-ranges/
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        ret = 0
        def checkRange(nums, startidx):
            nonlocal ret
            endidx = startidx+1
            minval = nums[startidx]
            maxval = nums[startidx]
            while endidx<=len(nums)-1:
                if nums[endidx] > maxval:
                    maxval = nums[endidx]
                if nums[endidx] < minval:
                    minval = nums[endidx]
                ret += (maxval - minval)
                endidx += 1
        for startidx in range(len(nums)-1):
            checkRange(nums, startidx)
        return ret
                
        
