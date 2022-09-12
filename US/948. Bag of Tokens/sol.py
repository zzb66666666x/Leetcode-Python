# https://leetcode.com/problems/bag-of-tokens/
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        n = len(tokens)
        if n == 0:
            return 0
        if n == 1:
            return 0 if tokens[0] > power else 1
        score = 0
        tokens.sort()
        getpower = n-1
        getscore = 0
        while getpower >= getscore:
            print(power, getscore, getpower)
            if score >= 1:
                if tokens[getscore] > power:
                    if getscore == getpower:
                        break
                    score -= 1
                    power += tokens[getpower]
                    getpower -= 1
                else:
                    score += 1
                    power -= tokens[getscore]
                    getscore += 1
            else:
                if tokens[getscore] > power:
                    break
                score += 1
                power -= tokens[getscore]
                getscore += 1
        return score
