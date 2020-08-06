#   The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
#   (you may want to display this pattern in a fixed font for better legibility)
#   P   A   H   N
#   A P L S I I G
#   Y   I   R
#   And then read line by line: "PAHNAPLSIIGYIR"
#   Write the code that will take a string and make this conversion given a number of rows:
#   string convert(string s, int numRows);
#   Example 1:
#       Input: s = "PAYPALISHIRING", numRows = 3
#       Output: "PAHNAPLSIIGYIR"
#   Example 2:
#       Input: s = "PAYPALISHIRING", numRows = 4
#       Output: "PINALSIGYAHRPI"
#   Explanation:
#       P     I    N
#       A   L S  I G
#       Y A   H R
#       P     I

class Solution:
    def convert(self, s, numRows):
        """
        :param s: str
        :param numRows: int
        :return: str
        """
        max_idx = len(s) - 1
        if len(s) <= numRows or numRows == 1:
            return s

        result = ""
        for row in range(numRows):
            jump1 = (numRows - row - 1) * 2
            jump2 = row * 2

            cul = row
            result += s[cul]
            isJump1 = True
            while True:
                if row == 0:
                    jump = jump1
                elif row == numRows - 1:
                    jump = jump2
                else:
                    if isJump1:
                        jump = jump1
                        isJump1 = False
                    else:
                        jump = jump2
                        isJump1 = True
                cul += jump
                if cul <= max_idx:
                    result += s[cul]
                else:
                    break
        return result

