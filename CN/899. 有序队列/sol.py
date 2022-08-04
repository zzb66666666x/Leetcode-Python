
# https://leetcode.cn/problems/orderly-queue/
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        n = len(s)
        cs = [c for c in s]
        if k==1:
            ans = s
            for _ in range(n-1):
                self.swap(cs)
                ans = min(ans, ''.join(cs))
            return ans
        else:
            # must have ordered string
            return ''.join(sorted(cs))
    
    def swap(self, cs):
        tmp = cs[0]
        cs.pop(0)
        cs.append(tmp)
        


