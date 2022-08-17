# https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I":1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, '#':1001}
        tmp = []
        prev = '#'
        for c in s:
            val = values[c]
            if values[c] > values[prev]:
                tmp[-1] *= -1
            tmp.append(val)
            prev = c
        return sum(tmp)
