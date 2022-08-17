# https://leetcode.com/problems/nim-game/
class Solution:
# 1, 2, 3 I win
# 4 lose
# 5, 6, 7 I win
# 8 lose 
    def canWinNim(self, n: int) -> bool:
        return False if n%4==0 else True
