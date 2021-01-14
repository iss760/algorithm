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
            # 홀수 회문일 경우 (ex. "cdc")
            temp = self._longestPalindrome(s, i, i)
            res = temp if len(res) < len(temp) else res

            # 짝수 회문일 경우 (ex. "cddc")
            temp = self._longestPalindrome(s, i, i+1)
            res = temp if len(res) < len(temp) else res

        return res

    def _longestPalindrome(self, s, l, r):
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                l -= 1
                r += 1
            else:
                break
        return s[l+1:r]