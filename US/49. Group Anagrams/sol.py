# https://leetcode.com/problems/group-anagrams/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for s in strs:
            cnt = Counter(s)
            key = ""
            for i in range(ord('a'), ord('z')+1):
                c = chr(i)
                if c in cnt:
                    key += (c+str(cnt[c]))
            if key in m:
                m[key].append(s)
            else:
                m[key] = [s]
        return list(m.values())
