
# https://leetcode.cn/problems/car-pooling/
# method1: general solution
# class Solution:
#     def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
#         # sort based on the start pos
#         trips.sort(key=lambda x: x[1])
#         m = {}
#         num = 0
#         for t in trips:
#             popk = []
#             for k,v in m.items():
#                 if k <= t[1]:
#                     num -= v
#                     popk.append(k)
#             for k in popk:
#                 m.pop(k)
#             num += t[0]
#             if num > capacity:
#                 return False
#             m[t[2]] = m.get(t[2], 0) + t[0]
#         return True

# method2: diff array
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diffarr = [0 for _ in range(1001)]
        for t in trips:
            diffarr[t[1]] += t[0]
            diffarr[t[2]] -= t[0]
        num = 0
        for val in diffarr:
            num += val
            if num > capacity:
                return False
        return True
