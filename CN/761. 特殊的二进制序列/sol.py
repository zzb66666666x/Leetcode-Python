# https://leetcode.cn/problems/special-binary-string/
class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if len(s) <= 2:
            return s
        
        cnt = left = 0
        subs = list()

        for i, ch in enumerate(s):
            if ch == "1":
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    subs.append("1" + self.makeLargestSpecial(s[left+1:i]) + "0")
                    left = i + 1
        # print(subs)
        subs.sort(reverse=True)
        return "".join(subs)

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/special-binary-string/solution/te-shu-de-er-jin-zhi-xu-lie-by-leetcode-sb7ry/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
