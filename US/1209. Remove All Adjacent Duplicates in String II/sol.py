# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
# 迭代字符串：

# 如果当前字符与前一个相同，栈顶元素加 1。

# 否则，往栈中压入 1。
# 如果栈顶元素等于 k，则从字符串中删除这 k 个字符，并将 k 从栈顶移除。

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[]
        for i in s:
            if stack and stack[-1][0]==i and stack[-1][1]==k-1:
                stack.pop()
            elif stack and stack[-1][0]==i and stack[-1][1]<k:
                stack[-1][1]+=1
            else:
                stack.append([i,1])
         
        for i in range(len(stack)):
            stack[i]=stack[i][0]*stack[i][1]
        return "".join(stack)
                    
