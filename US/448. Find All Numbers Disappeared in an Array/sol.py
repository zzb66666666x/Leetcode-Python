# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # arr = [0 for i in range(n)]
        # for val in nums:
        #     arr[val-1] = 1
        # ret = []
        # for slot in arr:
        #     if slot == 0:
        #         ret.append(slot + 1)
        # return ret
        
        # O(1) solution with swap
        
        def swap(nums, a, b):
            tmp = nums[a]
            nums[a] = nums[b]
            nums[b] = tmp
             
        n = len(nums)
        for i in range(n):
            while nums[i] != i+1:
                swap(nums, i, nums[i]-1)
                if nums[nums[i]-1] == nums[i]:
                    break
        ret = []
        for i in range(n):
            if nums[i] != i+1:
                ret.append(i+1)
        return ret
