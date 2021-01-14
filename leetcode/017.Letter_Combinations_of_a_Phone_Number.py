# Given a string containing digits from 2-9 inclusive,
# return all possible letter combinations that the number could represent.
# A mapping of digit to letters (just like on the telephone buttons) is given below.
# Note that 1 does not map to any letters.
#
# Example:
#   Input: "23"
#   Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

from functools import reduce


class Solution:
    def letterCombinations(self, digits):
        """
        :param digits: str
        :return: list[str]
        """
        dic = {2: ["a", "b", "c"], 3: ["d", "e", "f"], 4: ["g", "h", "i"],
               5: ["j", "k", "l"], 6: ["m", "n", "o"], 7: ["p", "q", "r", "s"],
               8: ["t", "u", "v"], 9: ["w", "x", "y", "z"]}

        nums = map(int, [num for num in digits])
        res = [""] if digits else []
        # 모든 경우의 수 조합
        for n in nums:
            res = [p + q for p in res for q in dic[n]]
        return res


sol = Solution()
print(sol.letterCombinations("23"))

