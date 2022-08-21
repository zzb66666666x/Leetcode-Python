# method1: my method
# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         if len(str2) > len(str1):
#             return self.gcdOfStrings(str2, str1)
#         def check(s, t):
#             idx = 0
#             while idx<len(s):
#                 if s[idx] != t[idx % len(t)]:
#                     return False
#                 idx += 1
#             # print(t + ":" + str(idx))
#             idx -= 1
#             return True if idx%len(t) == len(t)-1 else False
#         minlen = len(str2)
#         ret = ""
#         for length in range(1, minlen+1):
#             tmp = str2[0:length]
#             # print(tmp)
#             if check(str1, tmp) and check(str2, tmp):
#                 ret = tmp
#         return ret

# method2: Euclidean Algorithm
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            return a if b==0 else gcd(b, a%b)
        if str1+str2 != str2+str1:
            return ""
        else:
            return str1[0: gcd(len(str1), len(str2))]
        
