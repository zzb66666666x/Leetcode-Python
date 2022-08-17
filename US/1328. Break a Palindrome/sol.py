# https://leetcode.com/problems/break-a-palindrome/
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""
        for i in range(ceil((n-1)/2)):
            if palindrome[i] != 'a':
                return palindrome[0 : i] + 'a' + palindrome[i+1 : n+1]
        # now a string full of a in left half 
        return palindrome[0:n-1] + "b"
