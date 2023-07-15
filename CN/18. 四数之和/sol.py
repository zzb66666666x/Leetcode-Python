class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        cnt = collections.Counter(nums)
        nums = sorted(cnt)
        res = []
        for i, ei in enumerate(nums):
            for j, ej in enumerate(nums[i:], i):
                for k, ek in enumerate(nums[j:], j):
                    el = target - ei - ej - ek
                    if el < ek:
                        break
                    if el not in cnt:
                        continue
                    sub_cnt = collections.Counter([ei, ej, ek, el])
                    if all(cnt[k] >= sub_cnt[k] for k in sub_cnt):
                        res.append([ei, ej, ek, el])
        return res
