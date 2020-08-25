# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
#   Input: ["flower","flow","flight"]
#   Output: "fl"
# Example 2:
#   Input: ["dog","racecar","car"]
#   Output: ""
#   Explanation: There is no common prefix among the input strings.


class Solution:
    def longestCommonPrefix(self, str_ls):
        """
        :param str_ls: list[str]
        :return: str
        """
        prefix = ""
        if len(str_ls) == 0:
            return prefix

        for i in range(len(min(str_ls))):
            temp = str_ls[0][i]
            if all(_s[i] == temp for _s in str_ls):
                prefix += temp
            else:
                break
            print(prefix)
        return prefix


sol = Solution()
print(sol.longestCommonPrefix(["flower", "flow", "flight"]))