# https://leetcode.com/problems/find-and-replace-pattern/
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ret = []
        for s in words:
            if self.matchPattern(s, pattern):
                ret.append(s)
        return ret
        
    def matchPattern(self, s, p):
        if len(s) != len(p):
            return False
        map1 = {}
        map2 = {}
        for i in range(len(s)):
            sc = s[i]
            pc = p[i]
            if (sc in map1) and (pc in map2):
                if map1[sc] != map2[pc]:
                    return False
                else:
                    map1[sc]=i
                    map2[pc]=i
            elif (sc not in map1) and (pc not in map2):
                map1[sc] = i
                map2[pc] = i
            else:
                return False
        return set(map1.values())==set(map2.values())
