# https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/

# my first method
# class Solution:
#     def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
#         properties.sort(key=lambda x: x[0])
#         # print(properties)
#         n = len(properties)
#         attackval = properties[-1][0]
#         defenseval = properties[-1][1]
#         higherattack = attackval
#         higherdefense = defenseval
#         prevattack = attackval
#         cnt = 0
#         for i in range(n-2, -1, -1):
#             if properties[i][0] < prevattack:
#                 higherdefense = defenseval
#                 higherattack = attackval
#             if properties[i][1] > defenseval:
#                 attackval = properties[i][0]
#                 defenseval = properties[i][1]
#             if properties[i][0] < higherattack and properties[i][1] < higherdefense:
#                 cnt += 1
#             prevattack = properties[i][0]
#         return cnt

# an even smarter way, but actually slower
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key= lambda x: (x[0], -x[1]))
        n = len(properties)
        maxdefense = -1
        cnt = 0
        for i in range(n-1, -1, -1):
            if properties[i][1] < maxdefense:
                cnt += 1
            maxdefense = max(properties[i][1], maxdefense)
        return cnt

    
