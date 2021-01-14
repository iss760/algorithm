# Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
# Return the quotient after dividing dividend by divisor.
# The integer division should truncate toward zero, which means losing its fractional part.
# For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

# Example 1:
#   Input: dividend = 10, divisor = 3
#   Output: 3
#   Explanation: 10/3 = truncate(3.33333..) = 3.
# Example 2:
#   Input: dividend = 7, divisor = -3
#   Output: -2
#   Explanation: 7/-3 = truncate(-2.33333..) = -2.

import math


class Solution:
    def divide(self, dividend, divisor):
        """
        :param dividend: int
        :param divisor: int
        :return: int
        """
        if divisor == 1:
            return dividend
        flag = (dividend < 0) is (divisor < 0)
        temp = math.log(abs(dividend)) - math.log(abs(divisor))
        temp = math.exp(temp)
        quo = math.trunc(temp)

        if not flag:
            quo = -quo

        return min(max(-2**31, quo), 2**31-1)


sol = Solution()
print(sol.divide(1000, 1))
print(sol.divide(-2147483648, -1))
print(sol.divide(7, 3))
print(sol.divide(10, 4))
