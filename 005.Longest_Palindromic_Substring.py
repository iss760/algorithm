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
        size = len(s)
        if size == 0:
            return s
        result = s[0]
        max_len = 0
        for i in range(size - 1):
            for j in range(i + 1, size):
                if self.isPalindrome(s[i:j + 1]) and max_len < len(s[i:j + 1]):
                    max_len = len(s[i:j + 1])
                    result = s[i:j + 1]
        return result

    def isPalindrome(self, s):
        for i in range(len(s) // 2):
            if s[i] != s[-1 - i]:
                return False
        return True
