# https://leetcode.com/problems/trapping-rain-water/

# brute force method: TLE
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         maxh = max(height)
#         ret = 0
#         for h in range(1, maxh+1):
#             leftidx = -1
#             for i in range(len(height)):
#                 if height[i]>=h:
#                     if leftidx < 0:
#                         leftidx = i
#                     else:
#                         ret += (i-leftidx-1)
#                         leftidx = i
#         return ret

# stack method
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         stack = []
#         current = 0
#         ret = 0
#         while (current < len(height)):
#             while len(stack)>0 and height[current] > height[stack[-1]]:
#                 waterlevel = height[stack[-1]]
#                 stack.pop()
#                 if len(stack) == 0:
#                     break
#                 distance = current - stack[-1] - 1
#                 walllevel = min(height[stack[-1]], height[current])
#                 ret += (distance * (walllevel - waterlevel)) 
#             stack.append(current)
#             current += 1
#         return ret     
                    
# dp method
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<=2:
            return 0
        max_left = [0 for i in range(len(height))]
        max_right = [0 for i in range(len(height))]
        for i in range(1, len(height)):
            max_left[i] = max(max_left[i-1], height[i-1])
        for j in range(len(height)-2, -1, -1):
            max_right[j] = max(max_right[j+1], height[j+1])
        ret = 0
        # print(max_left)
        # print(max_right)
        for i in range(1, len(height)-1):
            minheight = min(max_left[i], max_right[i])
            if minheight > height[i]:
                ret += minheight - height[i]
        return ret
        
            
