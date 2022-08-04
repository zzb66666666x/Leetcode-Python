# https://leetcode.cn/problems/minimum-subsequence-in-non-increasing-order/
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        valsum = sum(nums)
        retsum = 0
        nums.sort(reverse=True)
        ret = []
        for i in nums:
            retsum += i
            if retsum > (valsum-retsum):
                ret.append(i)
                return ret
            else:
                ret.append(i)
