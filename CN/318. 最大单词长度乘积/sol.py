
# https://leetcode.cn/problems/maximum-product-of-word-lengths/
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        map = {} # mask to word length
        for s in words:
            mask = 0
            for c in s:
                mask |= (1 << ord(c) - ord('a'))
            if (mask in map and len(s)>map[mask]) or (mask not in map):
                map[mask] = len(s)
        ret = 0
        for k in map.keys():
            for k2 in map.keys():
                if k != k2 and k&k2 == 0: ret = max(ret, map[k]*map[k2])
        return ret
