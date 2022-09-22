# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        stack= []
        m = {"(":")", "[": "]", "{": "}"}
        for c in s:
            if c in m:
                stack.append(c)
            else:
                if len(stack)==0:
                    return False
                top = stack[-1]
                if m[top] == c:
                    stack.pop()
                else:
                    return False
        if len(stack)>0:
            return False
        else:
            return True
