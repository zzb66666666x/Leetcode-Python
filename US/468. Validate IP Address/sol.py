# https://leetcode.com/problems/validate-ip-address/
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def checkV6(s):
            values = s.split(':')
            if len(values) != 8:
                return "Neither"
            for value in values:
                if len(value)>=1 and len(value)<=4:
                    for c in value:
                        cord = ord(c)
                        if not ((cord>=ord('0') and cord<=ord('9')) or (cord>=ord('a') and cord<=ord('f')) or (cord>=ord('A') and cord<=ord('F')) ):
                            return "Neither"
                else:
                    return "Neither"
            return 'IPv6'
        def checkV4(s):
            digits = s.split('.')
            if len(digits) != 4:
                return "Neither"
            for d in digits:
                if len(d)>1 and d[0] == '0':
                    return "Neither"
                if len(d)>3 or len(d)<1:
                    return "Neither"
                val = 0
                for j in d:
                    if ord(j)>=ord('0') and ord(j)<=ord('9'):
                        val = val*10 + int(j)
                        if val > 255:
                            return "Neither"
                    else:
                        return "Neither"
            return 'IPv4'
        if ':' in queryIP:
            return checkV6(queryIP)
        else:
            return checkV4(queryIP)
