# https://leetcode.com/problems/poor-pigs/
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        k = minutesToTest // minutesToDie
        return math.ceil(math.log(buckets, 2) / math.log(k+1, 2))
