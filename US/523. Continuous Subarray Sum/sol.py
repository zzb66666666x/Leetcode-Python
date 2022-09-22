# https://leetcode.com/problems/continuous-subarray-sum/
# solution ref: https://leetcode.cn/problems/continuous-subarray-sum/solution/gong-shui-san-xie-tuo-zhan-wei-qiu-fang-1juse/
# sum[j]−sum[i−1]=n∗k
# sum[j]/k - sum[i-1]/k = n => int
# so sum[j] and sum[i-1] must have the same value if apply %k
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        sums = [0 for i in range(n+1)]
        for i in range(1, n+1):
            sums[i] = sums[i-1] + nums[i-1]
        myset = set()
        for i in range(2, n+1):
            myset.add(sums[i-2]%k)
            if sums[i]%k in myset:
                return True
        return False
