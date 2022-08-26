# https://leetcode.com/problems/reordered-power-of-2/

def cmpAnagram(a, b):
    return sorted(a.items())==sorted(b.items())

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digitlen = len(str(n))
        anagram = Counter(str(n))
        anagramlist = []
        n = 1
        while True:
            if len(str(n))>digitlen:
                break
            elif len(str(n))==digitlen:
                anagramlist.append(Counter(str(n)))
            n = n << 1
        for tmp in anagramlist:
            if cmpAnagram(tmp, anagram):
                return True
        return False
