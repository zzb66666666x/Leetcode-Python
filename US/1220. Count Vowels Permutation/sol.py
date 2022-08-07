# https://leetcode.com/problems/count-vowels-permutation/
# method1: dp (my method)
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        prevList = {'a':['e', 'i', 'u'], 'e':['a', 'i'], 'i':['e', 'o'], 'o':['i'], 'u':['i', 'o']}
        cnt = {'a':1, 'e':1, 'i':1, 'o':1, 'u':1}
        cnt2 = cnt.copy()
        for _ in range(1, n):
            for c in ['a', 'e', 'i', 'o', 'u']:
                prev = prevList[c]
                acc = 0
                for p in prev:
                    acc += cnt[p]
                cnt2[c] = acc
            tmp = cnt
            cnt = cnt2
            cnt2 = tmp
        return sum(cnt.values()) % 1000000007
