# https://leetcode.cn/problems/exclusive-time-of-functions/
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        record = [0 for _ in range(n)]
        curtime = 0
        for log in logs:
            info = log.split(":")
            curtime = int(info[2])
            if info[1] == "start":
                if len(stack)>0:
                    funclog = stack[len(stack)-1]
                    deltaT = curtime - funclog[1]
                    stack[len(stack)-1][1] = curtime
                    record[funclog[0]] += deltaT
                stack.append([int(info[0]), curtime])
            else:
                curtime+=1
                funclog = stack.pop()
                if len(stack)>0:
                    stack[len(stack)-1][1] = curtime
                deltaT = curtime - funclog[1]
                record[funclog[0]] += deltaT
            # print(stack, end="    ")
            # print(record)
        return record
