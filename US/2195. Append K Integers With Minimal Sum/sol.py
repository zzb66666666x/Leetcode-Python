# https://leetcode.cn/problems/append-k-integers-with-minimal-sum/
class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums.extend([0, int(2e9) + 1])
        nums.sort()

        presum = 0
        ans = 0
        for i in range(1, len(nums)):
            offer = nums[i] - nums[i - 1] - 1
            if offer > 0:
                if offer < k:
                    k -= offer
                else:
                    ans = (nums[i - 1] + k + 1) * (nums[i - 1] + k) // 2 - presum
                    break
            if nums[i] != nums[i - 1]:
                presum += nums[i]
        
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/append-k-integers-with-minimal-sum/solution/xiang-shu-zu-zhong-zhui-jia-k-ge-zheng-s-9vdv/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
