#   Given a string, find the length of the longest substring without repeating characters.
#   Example 1:
#       Input: "abcabcbb"
#       Output: 3
#       Explanation: The answer is "abc", with the length of 3.
#   Example 2:
#       Input: "bbbbb"
#       Output: 1
#       Explanation: The answer is "b", with the length of 1.
#   Example 3:
#       Input: "pwwkew"
#       Output: 3
#       Explanation: The answer is "wke", with the length of 3.
#                    Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


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
