# https://leetcode.com/problems/angle-between-hands-of-a-clock/
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minpercent = minutes/60
        mindegree = 360 * minpercent
        onehourdegree = (360/12)
        hourdegree = (hour % 12) * onehourdegree
        houroffset = onehourdegree * minpercent
        hourdegree += houroffset
        ret = abs(mindegree - hourdegree)
        return min(ret, 360-ret)
