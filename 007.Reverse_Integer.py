#Given a 32-bit signed integer, reverse digits of an integer.
#   Example 1:
#       Input: 123
#       Output: 321
#   Example 2:
#       Input: -123
#       Output: -321
#   Example 3:
#       Input: 120
#       Output: 21


class Solution:
    def reverse(self, x)
        """
        :param x: int 
        :return: int
        """
        if x <= -2 ** 31 or x >= 2 ** 31 - 1:
            return 0

        if x < 0:
            result = int(str(x * (-1))[::-1]) * (-1)
        else:
            result = int(str(x)[::-1])

        if result <= -2 ** 31 or result >= 2 ** 31 - 1:
            return 0
        else:
            return result

