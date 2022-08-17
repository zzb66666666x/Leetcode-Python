
# https://leetcode.com/problems/k-diff-pairs-in-an-array/
# method1: without binary search
# class Solution:
#     def findPairs(self, nums: List[int], k: int) -> int:
#         if k==0:
#             cnt = Counter(nums)
#             ret = 0
#             for k,v in cnt.items():
#                 if v>=2:
#                     ret+=1
#             return ret
#         nums = list(set(nums))
#         nums.sort()
#         # ans = set()
#         # print(nums)
#         ret = 0
#         for i in range(1, len(nums)):
#             idx = i-1
#             tmp = k
#             while idx>=0 and tmp>0:
#                 tmp -= (nums[idx+1] - nums[idx])
#                 if tmp == 0:
#                     # print(nums[idx], nums[i])
#                     # ans.add((nums[i], nums[idx]))
#                     ret += 1
#                     break
#                 idx -= 1
#         # return len(ans)
#         return ret

# method2: with binary search
# class Solution:
#     def findPairs(self, nums: List[int], k: int) -> int:
#         if k==0:
#             cnt = Counter(nums)
#             ret = 0
#             for k,v in cnt.items():
#                 if v>=2:
#                     ret+=1
#             return ret
#         nums = list(set(nums))
#         nums.sort()
#         ret = 0
#         for i in range(1, len(nums)):
#             l, r = 0, i-1
#             while l<=r:
#                 if l==r:
#                     ret += (1 if nums[l]+k == nums[i] else 0)
#                     break
#                 mid = (l+r)//2
#                 if nums[mid]+k == nums[i]:
#                     ret += 1
#                     break
#                 elif nums[mid]+k > nums[i]:
#                     r = mid-1
#                 else:
#                     l = mid+1
#         return ret

# method3: use map
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        m = {}
        for val in nums:
            m[val] = m.get(val, 0) + 1
        ret = 0
        for key,val in m.items():
            if k>0 and key+k in m or (k==0 and m.get(key)>1):  
                ret += 1
        return ret
