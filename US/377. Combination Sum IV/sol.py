# recur method: correct but too slow, use dp to make it better
# class Solution:
#     def combinationSum4(self, nums: List[int], target: int) -> int:
#         if len(nums)==1:
#             return 1 if nums[0] == target else 0
#         nums.sort()
#         self.cnt = 0
#         def recur(nums, target):
#             if target == 0:
#                 self.cnt += 1
#                 return 1
#             if target < 0:
#                 return -1
#             l,r = 0, len(nums)-1
#             ans = -1
#             if target >= nums[-1]:
#                 ans = r
#             elif nums[0] > target:
#                 return -1
#             else:
#                 while l<=r:
#                     if l==r:
#                         tmp = l if nums[l] <= target else -1
#                         ans = max(tmp, ans)
#                         break
#                     mid = (l+r)//2
#                     if nums[mid] < target:
#                         l = mid+1
#                         ans = max(ans, mid)
#                     elif nums[mid] == target:
#                         ans = mid
#                         break
#                     else:
#                         r = mid-1
#             if ans < 0:
#                 return -1
#             else:
#                 # print(ans)
#                 for i in range(ans+1):
#                     ret = recur(nums, target-nums[i])
#                     if ret < 0:
#                         break
#             return 1
#         recur(nums, target)
#         return self.cnt

# method1: dp
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        dp = [0] * (target+1)
        dp[0] = 1
        for i in range(1,target+1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i-num]
        return dp[target]
