# https://leetcode.com/problems/merge-intervals/
# method1: using queue
# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         if len(intervals)==1:
#             return intervals
#         intervals.sort(key = lambda x: x[0])
#         tmp = intervals[0]
#         tmp[0] -= 1
#         minval = tmp[0]
#         mergecnt = 0
#         q = deque(intervals[1:len(intervals)])
#         while True:
#             if len(q) == 0:
#                 q.append(tmp)
#                 break
#             head = q.popleft()
#             # print(head)
#             if head[0] == minval:
#                 q.append(tmp)
#                 if mergecnt == 0:
#                     q.appendleft(head)
#                     break
#                 mergecnt = 0
#                 tmp = head
#                 # print("finish", q)
#                 continue
#             # check if we can merge
#             if tmp[1]>=head[0]:
#                 mergecnt += 1
#                 tmp = [tmp[0], max(tmp[1], head[1])]
#                 # print("merge", q)
#             else:
#                 q.append(tmp)
#                 # print("cannot merge", q)
#                 tmp = head
#         ret = list(q)
#         ret[0][0] += 1
#         return ret
    
# method2: official sol
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
