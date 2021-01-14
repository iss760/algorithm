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
        for i in range(len(s)):
            temp.append(s[i])
            if len(temp) > max_long:
                max_long = len(temp)

            # 다음 원소가 temp에 있을 경우
            if i != len(s) - 1 and s[i + 1] in temp:
                # 첫번째 원소를 뺀 나머지로 리스트 구성
                temp = temp[temp.index(s[i + 1]) + 1:]

        return max_long


sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcaaw"))
