# method1: stack simulation
# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         n = len(s)
#         match = [0 for i in range(n)]
#         stack = []
#         for i in range(n):
#             if s[i] == '(':
#                 stack.append(i)
#             else:
#                 if len(stack)> 0:
#                     popval = stack.pop()
#                     match[popval] = 1
#                     match[i] = 1
#         lastone = -1
#         ret = 0
#         # print(match)
#         for i in range(n):
#             if match[i] == 1:
#                 if lastone < 0:
#                     lastone = i
#             if match[i] == 0:
#                 if lastone >= 0:
#                     ret = max(ret, i-lastone)
#                 lastone = -1
#         if lastone>=0:
#             ret = max(ret, n-lastone)
#         return ret

# method2: greedy
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left, right, maxlen = 0,0,0
        n = len(s)
        for i in range(n):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if right > left:
                left, right = 0,0
            elif left == right:
                maxlen = max(maxlen, 2*right)
        left, right = 0,0
        for i in range(n-1, -1, -1):
            if s[i] == ")":
                right += 1
            else:
                left += 1
            if left > right:
                left, right = 0, 0
            elif left == right:
                maxlen = max(maxlen, 2*right)
        return maxlen
                
            

