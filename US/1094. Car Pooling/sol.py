# https://leetcode.com/problems/car-pooling/
# method1: brute force
# class Solution:
#     def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
#         load = [0 for _ in range(1001)]
#         for trip in trips:
#             for i in range(trip[1], trip[2]):
#                 load[i] += trip[0]
#                 if load[i] > capacity:
#                     return False
#         return True

# method2: we can only use incremental / decremental
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        delta = [0 for _ in range(1001)]
        for trip in trips:
            delta[trip[1]] += trip[0]
            delta[trip[2]] -= trip[0]
        num =  0
        for val in delta:
            num += val
            if num > capacity:
                return False
        return True
