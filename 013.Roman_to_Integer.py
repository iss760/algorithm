# For example, two is written as II in Roman numeral, just two one's added together.
# Twelve is written as, XII, which is simply X + II.
# The number twenty seven is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is written as IV.
# Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX.
# There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
# Example 5:
#   Input: "MCMXCIV"
#   Output: 1994
#   Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


class Solution:
    def romanToInt(self, s):
        """
        :param s: str
        :return: int
        """
        romans = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        res = 0
        for i in range(len(s)):
            # 마지막 문자일경우
            if i == len(s) - 1:
                res += romans[s[i]]
            # like, CM: 1000-100, IV: 5-1
            elif romans[s[i]] < romans[s[i+1]]:
               res -= romans[s[i]]
            else:
                res += romans[s[i]]
        return res


sol = Solution()
print(sol.romanToInt("MCMXCIV"))
print(sol.romanToInt("DCXXI"))

