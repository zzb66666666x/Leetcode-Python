# https://leetcode.com/problems/merge-intervals/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==1:
            return intervals
        intervals.sort(key = lambda x: x[0])
        tmp = intervals[0]
        tmp[0] -= 1
        minval = tmp[0]
        mergecnt = 0
        q = deque(intervals[1:len(intervals)])
        while True:
            if len(q) == 0:
                q.append(tmp)
                break
            head = q.popleft()
            # print(head)
            if head[0] == minval:
                q.append(tmp)
                if mergecnt == 0:
                    q.appendleft(head)
                    break
                mergecnt = 0
                tmp = head
                # print("finish", q)
                continue
            # check if we can merge
            if tmp[1]>=head[0]:
                mergecnt += 1
                tmp = [tmp[0], max(tmp[1], head[1])]
                # print("merge", q)
            else:
                q.append(tmp)
                # print("cannot merge", q)
                tmp = head
        ret = list(q)
        ret[0][0] += 1
        return ret
