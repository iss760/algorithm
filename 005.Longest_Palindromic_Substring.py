#   Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#   Example 1:
#       Input: "babad"
#       Output: "bab"
#       Note: "aba" is also a valid answer.
#   Example 2:
#       Input: "cbbd"
#       Output: "bb"


class Solution:
    def longestPalindrome(self, s):
        """
        :param s: str
        :return: str
        """
        if len(s) == 1:
            return s[0]

        res = ""
        for i in range(len(s)):
            temp = s[i]
            l, r = -1, 1

            while l+i >= 0 and r+i <= len(s)-1:
                if s[i+l] == s[i+r]:
                    temp = s[i+l] + temp + s[i+r]
                    l -= 1
                    r += 1
                else:
                    break

            res = temp if len(res) < len(temp) else res

        for i in range(len(s) - 1):
            if s[i] != s[i+1]:
                continue
            temp = s[i:i+2]
            l, r = -1, 1

            while l+i >= 0 and i+1+r <= len(s)-1:
                if s[i+l] == s[i+1+r]:
                    temp = s[i+l] + temp + s[i+1+r]
                    l -= 1
                    r += 1
                else:
                    break

            res = temp if len(res) < len(temp) else res

        return res


sol = Solution()
print(sol.longestPalindrome("babad"))
print(sol.longestPalindrome(''))
print(sol.longestPalindrome("aaaa"))
print(sol.longestPalindrome("aaabaaaa"))

