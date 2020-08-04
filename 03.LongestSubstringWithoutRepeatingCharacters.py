class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :param s: string
        :return: int
        """
        temp = []
        max_long = 0
        for idx in range(len(s)):
            temp.append(s[idx])
            if len(temp) > max_long:
                max_long = len(temp)

            if idx != len(s) - 1 and s[idx + 1] in temp:
                temp = temp[temp.index(s[idx + 1]) + 1:]
        return max_long

sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcaaw"))
