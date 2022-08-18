# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
# binary search method
# class Solution:
#     def numPairsDivisibleBy60(self, time: List[int]) -> int:
#         def target(lower, upper, val):
#             start = ceil(lower / 60)*60
#             ret = []
#             while start <= upper:
#                 ret.append(start - val)
#                 start += 60
#             return ret
#         if len(time) == 1:
#             return 0
#         tmp = []
#         cnt60 = 0
#         for val in time:
#             if val % 60 == 0:
#                 cnt60 += 1
#             else:
#                 tmp.append(val)
#         time = tmp
#         time.sort()
#         ans = cnt60 * (cnt60-1) // 2
#         for i in range(1, len(time)):
#             lower = time[i]
#             upper = 2 * time[i]
#             targets = target(lower, upper, time[i])
#             # print(targets)
#             for t in targets:
#                 l, r = 0, i-1
#                 while l<=r:
#                     if l==r:
#                         ans += (1 if time[l] == t else 0)
#                         break
#                     mid = (l+r)//2
#                     if time[mid] == t:
#                         ans += 1
#                         idx = mid+1
#                         while idx <= r:
#                             if time[idx] == t:
#                                 ans += 1
#                             else:
#                                 break
#                             idx += 1
#                         idx = mid - 1
#                         while idx >= l:
#                             if time[idx] == t:
#                                 ans += 1
#                             else:
#                                 break
#                             idx -= 1
#                         break
#                     elif time[mid] < t:
#                         l = mid+1
#                     else:
#                         r = mid-1
#             # print(i, ans)
#         return ans
            
# hashmap method
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        m = {}
        ans = 0
        for i in range(len(time)):
            val = time[i] % 60
            a = 60 if val % 60 == 0 else val % 60
            if 60-a in m:
                ans += m[60-a]
            tmp = m.get(val, 0)
            m[val] = tmp + 1
        return ans
